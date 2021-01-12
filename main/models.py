from django.db import models
from django.utils import timezone


class Property(models.Model):
    bill_number = models.CharField(unique=True, max_length=255, null=False)
    bill = models.CharField(max_length=255, null=False)
    congress = models.CharField(max_length=255, null=False)
    date = models.CharField(max_length=255, null=False)
    link = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.bill

