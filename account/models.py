from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUser(AbstractUser):
    groups = None
    user_permissions = None

    # EMAIL_FIELD = 'email'
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']


# class CustomManager(UserManager):
#     pass
