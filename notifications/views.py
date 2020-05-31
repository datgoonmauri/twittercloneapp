from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from notifications.models import Notification
from twitteruser.models import TwitterUser
from django.db.models.signals import post_save


from notifications.models import Notification


@login_required
def notification(request):
    current_user = TwitterUser.objects.get(username=request.user)
    notifications = Notification.objects.filter(notified_user=current_user, viewed=False)
    for notif in notifications:
        if current_user.notifications.unread():
            notif.viewed = True
            notif.save()
    return render(request, 'notifications.html', {'notifications': notifications})