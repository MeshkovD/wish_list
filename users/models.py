from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel


class CustomUser(BaseModel, User):
    profile = models.OneToOneField(
        "Profile",
        on_delete=models.CASCADE,
        related_name="custom_user",
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Profile(BaseModel):
    user = models.OneToOneField(
        "CustomUser",
        on_delete=models.PROTECT,
        related_name="profile_info",
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
