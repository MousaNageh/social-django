from djongo import models
from django.urls import reverse
from django.contrib.auth.models import User as auth_user, PermissionsMixin
from django.conf import settings
import os
from django.utils import timezone
from django.core import validators
from django.db.models import Q
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

    def friends_ids(self):
        friends_ids = []
        friends = FriendRequest.objects.filter(Q(approved=True) & (Q(
            from_user_id=self.id) | Q(to_user_id=self.id)))
        for friend in friends:
            if friend.to_user.id != self.id:
                friends_ids.append(friend.to_user.id)
            if friend.from_user.id != self.id:
                friends_ids.append(friend.from_user.id)
        return friends_ids


class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name='to_user', on_delete=models.CASCADE)
    request_date = models.DateTimeField(default=timezone.now())
    approved = models.BooleanField(default=False)

    def approve_friend_request(self):
        self.approved = True


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255, validators=[validators.MaxLengthValidator(
        255, "post title must be less than 255 character .")])
    content = models.TextField()
    img = models.ImageField(upload_to="posts", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse("myapp:profile", kwargs={"pk": self.user.pk})

    def delete_img(self, name):
        os.remove(os.path.join(settings.MEDIA_ROOT, name))

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.content
