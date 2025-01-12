from django.db import models

from core.models import BaseModel


class WishList(BaseModel):
    user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="wish_list",
    )

    def __str__(self):
        return f"WishList for user {self.user}"

    class Meta:
        verbose_name = "WishList"
        verbose_name_plural = "WishLists"


class Wish(BaseModel):
    wish_list = models.ForeignKey(
        "WishList",
        on_delete=models.CASCADE,
        related_name="wishes",
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.SET_NULL,
        related_name="wishes",
        null=True,
    )

    class Meta:
        verbose_name = "Wish"
        verbose_name_plural = "Wishes"


class Product(BaseModel):
    name = models.CharField(
        max_length=50,
    )

    @property
    def all_links(self):
        return self.links.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Link(BaseModel):
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="links",
    )
    url = models.URLField()

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"

    def __str__(self):
        return self.url
