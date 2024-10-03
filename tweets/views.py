from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tweets.models import Tweet
from tweets.serializers import TweetSerializer

# Create your views here.
# @api_view(['GET'])
def tweets(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    # return Response(serializer.data)
    return JsonResponse(serializer.data, safe=False)

