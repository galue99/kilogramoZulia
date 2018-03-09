# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import Weight
# Create your models here.
class Verificacion(Weight):
    buenos = models.IntegerField(blank=True, null=True)
    malos = models.IntegerField(blank=True, null=True)
    provider = models.ForeignKey('accounts.Company', null=True, blank=True)
    weight = models.ForeignKey('accounts.Weight', null=True, blank=True)


    def __str__(self):
        return self.provider