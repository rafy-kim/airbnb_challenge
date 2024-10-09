from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from .models import Tweet

class TweetAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.tweet = Tweet.objects.create(payload='Test tweet', user=self.user)

    def test_get_tweets(self):
        url = reverse('tweets')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_tweet(self):
        url = reverse('tweets')
        data = {'payload': 'New test tweet'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tweet.objects.count(), 2)
        self.assertEqual(response.data['payload'], 'New test tweet')

    def test_get_tweet_detail(self):
        url = reverse('tweet-detail', kwargs={'pk': self.tweet.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['payload'], 'Test tweet')

    def test_update_tweet(self):
        url = reverse('tweet-detail', kwargs={'pk': self.tweet.pk})
        data = {'payload': 'Updated test tweet'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tweet.objects.get(pk=self.tweet.pk).payload, 'Updated test tweet')

    def test_delete_tweet(self):
        url = reverse('tweet-detail', kwargs={'pk': self.tweet.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tweet.objects.count(), 0)

    def test_update_tweet_unauthorized(self):
        other_user = User.objects.create_user(username='otheruser', password='otherpass')
        other_tweet = Tweet.objects.create(payload='Other tweet', user=other_user)
        url = reverse('tweet-detail', kwargs={'pk': other_tweet.pk})
        data = {'payload': 'Trying to update'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_tweet_unauthorized(self):
        other_user = User.objects.create_user(username='otheruser', password='otherpass')
        other_tweet = Tweet.objects.create(payload='Other tweet', user=other_user)
        url = reverse('tweet-detail', kwargs={'pk': other_tweet.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

