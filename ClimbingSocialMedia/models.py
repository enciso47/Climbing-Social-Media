# Do NOT change without confirming with team
import uuid

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True)
    picture = models.ImageField(default='defaultProfilePic.jpg', upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="comment_likes_users", blank=True)
    replies = models.ManyToManyField('self', symmetrical=False)
    description = models.CharField(max_length=500)
    media = models.ImageField(upload_to='', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="post_likes_users", blank=True)
    comments = models.ManyToManyField(Comment, related_name="post_comments_users", blank=True)
    description = models.CharField(max_length=500)
    media = models.ImageField(upload_to='', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
