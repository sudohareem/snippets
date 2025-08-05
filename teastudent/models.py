from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    account_choices = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    account_type = models.CharField(max_length=10 , choices=account_choices )
