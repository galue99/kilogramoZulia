# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-08 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180308_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='weight',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
