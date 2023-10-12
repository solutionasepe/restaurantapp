from typing import Any
from django.db import models
# from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _ 

# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_("Email field required"))

        email = self.normalize_email(email)
        user = self.model( email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("superuser must have staff = True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("superuser must have is_superuser = True."))
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username