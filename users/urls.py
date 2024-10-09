from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("", views.Users.as_view(), name='users'),
    path('<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/tweets/', views.UserTweetView.as_view(), name='user-tweets'),

    path('password/', views.ChangePassword.as_view(), name='change-password'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),

]
