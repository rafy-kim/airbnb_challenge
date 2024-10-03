from rest_framework import serializers

class TweetSerializer(serializers.Serializer):
    payload = serializers.CharField(max_length=100)
    user_id = serializers.IntegerField()


