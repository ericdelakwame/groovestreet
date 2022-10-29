import django
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.pk})
