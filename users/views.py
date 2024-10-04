from rest_framework.response import Response
from rest_framework.views import APIView
from tweets.serializers import TweetSerializer
from users.models import User


class UserTweetView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            tweets = user.tweets.all()
            serializer = TweetSerializer(tweets, many=True)
            return Response(serializer.data)
        except:
            return Response({'error': 'User not found'}, status=404)
