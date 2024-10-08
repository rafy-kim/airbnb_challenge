from django.contrib import admin
from django.urls import path, include

from tweets import views as tweet_views

urlpatterns = [
    path('', tweet_views.TweetView.as_view(), name='tweets'),
    path('<int:pk>', tweet_views.TweetDetailView.as_view(), name='tweet-detail'),
]
