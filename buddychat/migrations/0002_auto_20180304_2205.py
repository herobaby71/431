# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_membership_owner'),
        ('buddychat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buddymessage',
            name='room',
        ),
        migrations.AddField(
            model_name='buddymessage',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='groups.Group'),
        ),
        migrations.AlterField(
            model_name='buddymessage',
            name='message',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='buddymessage',
            name='message_html',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
