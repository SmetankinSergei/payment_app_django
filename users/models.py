from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_ROLE = 'user'
    ADMIN_ROLE = 'admin'

    ROLE_CHOICES = [
        (USER_ROLE, 'User'),
        (ADMIN_ROLE, 'Admin'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER_ROLE)

    def is_admin(self):
        return self.role == self.ADMIN_ROLE
