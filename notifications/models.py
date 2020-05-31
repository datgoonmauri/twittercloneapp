import notify
from django.db import models
from django.db.models.signals import post_save

from twitteruser.models import TwitterUser
from tweets.models import Tweet


class Notification(models.Model):
    notified_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
