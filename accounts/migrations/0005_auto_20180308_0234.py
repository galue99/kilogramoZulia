# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-08 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180308_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='model_pic',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='model_pic',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
