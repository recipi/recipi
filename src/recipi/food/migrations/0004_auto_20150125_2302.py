# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_fooddescription_manufacturer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooddescription',
            name='survey',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
    ]
