# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-02 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180129_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user/'),
        ),
        migrations.AddField(
            model_name='user',
            name='faceboookAvatar',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
