from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email address")
    phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="phone number"
    )
    city = models.CharField(max_length=20, blank=True, null=True, verbose_name="city")
    avatar = models.ImageField(
        upload_to="users/avatars", null=True, blank=True, verbose_name="avatar"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
