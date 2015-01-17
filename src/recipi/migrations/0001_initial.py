# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import recipi.utils.db.uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('id', recipi.utils.db.uuid.UUIDField(editable=False, serialize=False, max_length=32, unique=True, primary_key=True, blank=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='Email')),
                ('name', models.TextField(max_length=100, verbose_name='Name')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'verbose_name': 'User',
            },
            bases=(models.Model,),
        ),
    ]
