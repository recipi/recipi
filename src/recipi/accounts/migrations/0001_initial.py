# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import recipi.utils.db.uuid
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('id', recipi.utils.db.uuid.UUIDField(editable=False, max_length=32, serialize=False, primary_key=True, unique=True, blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email', unique=True)),
                ('name', models.TextField(max_length=100, verbose_name='Name')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            bases=(models.Model,),
        ),
    ]
