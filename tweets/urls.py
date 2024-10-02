from django.contrib import admin
from django.urls import path, include

from tweets import views as tweet_views

urlpatterns = [
    path('', tweet_views.tweets, name='tweets'),
]
