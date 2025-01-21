from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.email