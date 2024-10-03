from django.contrib import admin
from django.urls import path, include

from users import views as user_views

urlpatterns = [
    path('<user_id>/tweets/', user_views.user_tweets, name='user_tweets'),
]
