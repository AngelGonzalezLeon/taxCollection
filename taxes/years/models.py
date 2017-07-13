# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Year2013(models.Model):
    GeoName = models.CharField(max_length=200)
    Year = models.CharField(max_length=200)
    Total_Tax = models.CharField(max_length=200)
    Property_Tax = models.CharField(max_length=200)
    Sales_Tax = models.CharField(max_length=200)
    License_Tax = models.CharField(max_length=200)
    Income_Tax = models.CharField(max_length=200)
    Other_Tax = models.CharField(max_length=200)

    def __str__(self):
            return self.GeoName + " " + self.Year
