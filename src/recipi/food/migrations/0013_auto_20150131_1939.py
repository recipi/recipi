# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0012_remove_languagedescription_countries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languagedescription',
            name='factor_code',
            field=models.CharField(unique=True, max_length=5),
            preserve_default=True,
        ),
    ]
