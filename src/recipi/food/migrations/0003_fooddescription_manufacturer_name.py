# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20150125_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooddescription',
            name='manufacturer_name',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
