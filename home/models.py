from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pics', default='profile_pics/default.jpg')

    bio = models.TextField(blank=True)

    def __str__(self):
        return (self.user.username)

    def save_user(self):
        self.save()
