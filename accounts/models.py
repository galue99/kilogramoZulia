from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db.models import signals
from django.db import models
from django.utils.crypto import get_random_string
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    dni = models.IntegerField(unique=True, blank=True, null=True)
    position = models.CharField(max_length=140, null=True, blank=True)
    alias = models.CharField(max_length=140, null=True, blank=True)
    branch_office = models.CharField(max_length=140, blank=True, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name="company", null=True, blank=True)
    model_pic = models.ImageField(upload_to = 'media/')

    def __str__(self):
        return self.username


class Company(models.Model):
    name = models.CharField(max_length=140, blank=True, null=True)
    rif = models.CharField(max_length=140, blank=True, null=True)
    phone = models.CharField(max_length=140, blank=True, null=True)
    email = models.CharField(max_length=140, blank=True, null=True)
    address = models.TextField(max_length=255, blank=True, null=True)
    model_pic = models.ImageField(upload_to = 'media/')


    def __str__(self):
        return self.name


class Weight(models.Model):
    PENDING= "pendig"
    APROVE = "aprove"
    RECHAZADO = "rechazado"
    TYPE_STATUS = (
        (PENDING,_("pendig")),
        (APROVE, _("aprove")),
        (RECHAZADO,_("rechazado")),
    )

    user = models.ForeignKey('User', null=True, blank=True)
    weight1 = models.CharField(max_length=140, null=True, blank=True)
    weight2 = models.CharField(max_length=140, null=True, blank=True)
    weight3 = models.CharField(max_length=140, null=True, blank=True)
    weight4 = models.CharField(max_length=140, null=True, blank=True)
    weight5 = models.CharField(max_length=140, null=True, blank=True)
    provider = models.ForeignKey('Company', null=True, blank=True)
    date = models.DateField(auto_now=True)
    time = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=140, null=True, blank=True)
    status = models.BooleanField(default=False)
    statuss = models.CharField(max_length=50,choices=TYPE_STATUS, default=PENDING)

    class Meta:
        abstract = True

    def __str__(self):
        return self.user.username
