# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 03:10
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, null=True, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('admin', models.BooleanField(default=False, verbose_name='admin status')),
                ('firstName', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('lastName', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=55, max_digits=60, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=55, max_digits=60, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('status', models.IntegerField(choices=[(0, 'Free'), (1, 'Chill'), (2, 'Away'), (3, 'Busy'), (4, 'Hidden'), (5, 'Sleeping')], default=0)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user/')),
                ('faceboookAvatar', models.CharField(blank=True, max_length=500, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
