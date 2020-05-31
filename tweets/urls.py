from django.contrib import admin
from django.urls import path
from tweets import views

urlpatterns = [
    path('addtweet/<int:user_id>', views.addtweet, name='add_tweet'),
    path('tweet/<int:tweet_id>', views.tweetview, name='tweet'),
]