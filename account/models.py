from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_image = models.ImageField(default='', upload_to='profile_pic')
    EMAIL_FIELD = 'email'
    USERNAME_FIELD='username'
    REQUIRED_FIELDS = ['email']


# class CustomManager(UserManager):
#     pass
