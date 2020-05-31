from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse
from notifications.models import Notification
from tweets.models import Tweet
from twitteruser.models import TwitterUser


@login_required
def index(request):
	html = 'index.html'
	user_data = TwitterUser.objects.all()
	tweet_data = Tweet.objects.all()
	return render(request, html, {'tweet_data': tweet_data, "user_data": user_data})


def profileview(request, user_id):
	user_tweets = Tweet.objects.filter(author=user_id)
	twitteruser = TwitterUser.objects.get(id=user_id)
	following_list = twitteruser.following.all()
	following_count = following_list.count()
	tweet_count = user_tweets.count()
	if request.user.is_authenticated:
		following_list = request.user.following.all()
		if twitteruser in following_list:
			is_following = True
		else:
			is_following = False
		return render(
			request,
			'profile.html', {
				'user_tweets': user_tweets,
				'twitteruser': twitteruser,
				'is_following': is_following,
				'following_count': following_count,
				'tweet_count': tweet_count,
				'following_list': following_list,
			})
	return HttpResponseRedirect(reverse("homepage"))


@login_required
def user_to_follow(request, id):
	current_user = request.user
	follow_user = TwitterUser.objects.get(id=id)
	current_user.following.add(follow_user)
	current_user.save()
	return HttpResponseRedirect(reverse('profile', kwargs={'user_id': id}))


@login_required
def unfollow_user(request, id):
	current_user = request.user
	follow_user = TwitterUser.objects.get(id=id)
	current_user.following.remove(follow_user)
	current_user.save()
	return HttpResponseRedirect(reverse('profile', kwargs={'user_id': id}))

