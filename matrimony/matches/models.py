from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse
from datetime import date
import datetime
from django.conf import settings
from django.utils import dateformat
from django.utils.timesince import timesince
#import tensorflow as tf

class BiodataModel(models.Model):
    name = models.CharField(max_length=100, default='')
    contact = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100,default='')
    place_of_birth = models.CharField(max_length=100, default='')
    sub_place = models.CharField(max_length=100, default='')
    dob = models.DateField(blank=True, null=True, default='2020-01-01')
    timeofBirth = models.DateField(blank=True, null=True, default='2020-01-01')
    caste = models.CharField(max_length=100, default='')
    sub_caste = models.CharField(max_length=100, default='')
    gotra = models.CharField(max_length=100, default='')
    manglik = models.CharField(max_length=100, default='')
    rashi = models.CharField(max_length=100, default='')
    nakshatra = models.CharField(max_length=100, default='')
    height = models.CharField(max_length=100, default='')
    religion = models.CharField(max_length=100, default='')
    education = models.CharField(max_length=100, default='')
    employee = models.CharField(max_length=100, default='')
    income = models.CharField(max_length=100, default='')
    college_name = models.CharField(max_length=100, default='')
    org_name = models.CharField(max_length=100, default='')
    fname = models.CharField(max_length=100, default='')
    mname = models.CharField(max_length=100, default='')
    foccupation = models.CharField(max_length=100, default='')
    moccupation = models.CharField(max_length=100, default='')
    brothers = models.CharField(max_length=100, default='')
    sisters = models.CharField(max_length=100, default='')
    mbrothers = models.CharField(max_length=100, default='')
    msisters = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')