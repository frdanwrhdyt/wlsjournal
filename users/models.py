from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE = (
        ('OWNER', 'Owner'),
        ('ADMIN', 'Admin'),
        ('CASSIER', 'Cassier')
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100, choices=ROLE, default='OWNER')

    def __str__(self):
        return self.username
