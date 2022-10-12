from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, unique=True)
    favorites = models.ManyToManyField('api.Book', related_name="added_to_favorite")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
