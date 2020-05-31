from django import forms
from tweets.models import Tweet


class AddTweet(forms.ModelForm):
	class Meta:
		model = Tweet
		fields = ['tweet']
