from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import EmployeeManager
from django import utils

shift_choices = (('zero', '0'), ('one', '1'), ('two', '2'),
                 ('three', '3'), ('four', '4'))


class Employee(AbstractUser):
    company = models.TextField(max_length=100)
    shift = models.CharField(max_length=6, choices=shift_choices, default='1')

    objects = EmployeeManager()
