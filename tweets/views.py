from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from tweets.models import Tweet
from tweets.forms import AddTweet
from twitteruser.models import TwitterUser
from notifications.models import Notification

import re


@login_required
def addtweet(request, user_id):
	form = AddTweet()
	if request.method == 'POST':
		form = AddTweet(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			all_user = TwitterUser.objects.all()
			user = TwitterUser.objects.get(id=user_id)
			tweet = Tweet.objects.create(
				tweet=data['tweet'],
				author=user,
			)
			regex_users = re.findall(r'@(\w+)', data['tweet'])
			for tag in regex_users:
				Notification.objects.create(notify_user=TwitterUser.objects.get(username=tag),tweet=tweet)
			return HttpResponseRedirect(reverse('homepage'))
	return render(request, "addtweet.html", {"form": form})


def tweetview(request, tweet_id):
	tweet = Tweet.objects.get(id=tweet_id).order_by('date')
	return render(request, 'tweet.html', {'tweet': tweet})
