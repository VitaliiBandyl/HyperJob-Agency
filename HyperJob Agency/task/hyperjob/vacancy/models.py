from django.contrib.auth.models import User
from django.db import models


class Vacancy(models.Model):
    """Vacancy model"""
    description = models.TextField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
