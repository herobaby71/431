# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_membership_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.CharField(default='awesome group', max_length=255),
        ),
    ]
