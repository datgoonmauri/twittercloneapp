from django.urls import path
from twitteruser import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/<int:user_id>', views.profileview, name='profile'),
    path('user_to_follow/<int:id>', views.user_to_follow, name='follow'),
    path('unfollow_user/<int:id>', views.unfollow_user, name='unfollow'),
]
