from rest_framework.response import Response
from rest_framework.views import APIView
from tweets.serializers import TweetSerializer
from users.models import User
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import NotFound, ParseError
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from time import sleep
from users import serializers



class Users(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = serializers.TinyUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError("password is required")
        if not isinstance(password, str):
            raise ParseError("password is not string")
        serializer = serializers.DetailUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = serializers.DetailUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class UserDetailView(APIView):

    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = serializers.DetailUserSerializer(user)
            return Response(serializer.data)
        except:
            return Response({'error': 'User not found'}, status=404)
        


class UserTweetView(APIView):

    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            tweets = user.tweets.all()
            serializer = TweetSerializer(tweets, many=True)
            return Response(serializer.data)
        except:
            return Response({'error': 'User not found'}, status=404)




class ChangePassword(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            raise ParseError("old_password and new_password are required")
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            raise ParseError("wrong password")


class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError("username and password are required")
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response({"ok": "Welcome!"})
        else:
            return Response(
                {"error": "wrong password"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LogOut(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        sleep(2)
        logout(request)
        return Response({"ok": "bye!"})


