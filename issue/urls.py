from django.contrib import admin
from django.urls import path
from .views import signup_view

from .views import CustomObtainAuthToken, UserListAPI, ProjectAPI, IssueAPI

urlpatterns = [
    path('signup',signup_view,name="signup_view"),
    path('login',CustomObtainAuthToken.as_view(), name="login"),
    path('userlist', UserListAPI.as_view()),
    path('project', ProjectAPI.as_view()),
    path('project/<int:pk>', ProjectAPI.as_view()),
    path('issue', IssueAPI.as_view()),
    path('issue/<int:pk>', IssueAPI.as_view())
]