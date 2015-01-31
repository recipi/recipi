# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_auto_20150131_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='weight',
            name='sequence',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
