# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20150125_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooddescription',
            old_name='refuse',
            new_name='refuse_percentage',
        ),
    ]
