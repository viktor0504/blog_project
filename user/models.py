from django.contrib.auth.models import AbstractUser

from django.db import models



class User(AbstractUser):
    email = models.EmailField('Email address', unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default = True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']