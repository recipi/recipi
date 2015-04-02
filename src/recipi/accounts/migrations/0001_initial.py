# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import recipi.utils.db.uuid
import recipi.accounts.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('id', recipi.utils.db.uuid.UUIDField(unique=True, max_length=32, blank=True, serialize=False, primary_key=True, editable=False)),
                ('email', models.EmailField(unique=True, max_length=256, verbose_name='Email')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'verbose_name': 'User',
            },
            managers=[
                ('objects', recipi.accounts.models.UserManager()),
            ],
        ),
    ]
