from django.db import models
from users.models import Employee

import uuid

# Create your models here.


class Entry(models.Model):

    owner = models.ForeignKey(
        Employee, to_field='username', null=True, blank=True, on_delete=models.CASCADE)
    company = models.TextField(max_length=100, null=True, blank=True)
    vehicle_no = models.TextField(max_length=30, null=True, blank=True)
    date = models.CharField(max_length=15)
    slip_no = models.CharField(max_length=100, primary_key=True)
    party_name = models.CharField(max_length=200)
    item = models.CharField(max_length=10)
    litre = models.CharField(max_length=10)
    amt = models.CharField(max_length=10)

    def __str__(self):
        return str(self.slip_no)


class Partyname(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        Employee, to_field='username', null=True, blank=True, on_delete=models.CASCADE)
    company = models.TextField(max_length=100, null=True, blank=True)
    party_name = models.CharField(max_length=200)


class Prices(models.Model):

    owner = models.ForeignKey(
        Employee, to_field='username', null=True, blank=True, on_delete=models.CASCADE)
    company = models.TextField(max_length=100)
    p_price = models.TextField(max_length=10, default=0)
    d_price = models.TextField(max_length=10, default=0)
    xp_price = models.TextField(max_length=10, default=0)
    s_price = models.TextField(max_length=10, default=0)

    def __str__(self):
        return str(self.company)
