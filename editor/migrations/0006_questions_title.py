# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0005_auto_20161013_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]