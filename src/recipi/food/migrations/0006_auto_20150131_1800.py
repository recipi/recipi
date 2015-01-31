# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20150131_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foonote',
            old_name='number',
            new_name='sequence',
        ),
    ]
