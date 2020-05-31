from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from authentication.forms import SignUpForm, LoginForm
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required


def signupview(request):
    html = 'signup.html'
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        new_user = TwitterUser.objects.create_user(
            username=data['username'],
            password=data['password1'],
            )
        new_user.save()
        login(request, new_user)
        return HttpResponseRedirect(reverse('home'))
    form = SignUpForm()
    return render(request, html, {'form': form})


def loginview(request):
    html = 'login.html'
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'],
                password=data['password'])
            if user:
                login(request, user)
            return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, html, {'form': form})


@login_required
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))