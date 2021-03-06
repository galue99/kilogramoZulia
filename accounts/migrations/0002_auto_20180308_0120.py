# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-08 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rol',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='dni',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='first_name',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='last_name',
            new_name='rif',
        ),
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
