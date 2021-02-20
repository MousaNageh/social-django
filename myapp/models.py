from djongo import models
from django.urls import reverse
from django.contrib.auth.models import User as auth_user, PermissionsMixin
from django.conf import settings
import os
from django.utils import timezone
# Create your models here.


class User(auth_user):
    user_img = models.ImageField(
        upload_to="profile", null=True, blank=True)

    def get_absolute_url(self):
        return reverse("myapp:login")

    def __str__(self):
        return f'@{self.username}'

    def delete_img(self, name):
        os.remove(os.path.join(settings.MEDIA_ROOT, name))


class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name='to_user', on_delete=models.CASCADE)
    request_date = models.DateTimeField(default=timezone.now())
    approved = models.BooleanField(default=False)

    def approve_friend_request(self):
        self.approved = True
