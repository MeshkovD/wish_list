from django.contrib.auth.models import AbstractUser
from django.db import models

from core import settings
from core.models import BaseModel


class CustomUser(BaseModel, AbstractUser ):

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Profile(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="profile",
    )
    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
    )

    def __str__(self):
        return f"Profile for user {self.user.username}"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
