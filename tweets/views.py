from rest_framework.response import Response
from rest_framework.views import APIView
from tweets.models import Tweet
from tweets.serializers import TweetSerializer


class TweetView(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

