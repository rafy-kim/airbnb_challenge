from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from users.models import User

# Create your views here.
# @api_view(['GET'])
def user_tweets(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        tweets = user.tweets.all()
        serializer = TweetSerializer(tweets, many=True)
        # return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False)
    except:
        # return Response({'error': 'User not found'}, status=404)
        return JsonResponse({'error': 'User not found'}, status=404)
