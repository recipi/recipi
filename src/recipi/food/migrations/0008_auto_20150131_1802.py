# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20150131_1801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='long_description',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='short_description',
            new_name='short_name',
        ),
    ]
