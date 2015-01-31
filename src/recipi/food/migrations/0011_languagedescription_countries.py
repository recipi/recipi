# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_auto_20150131_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='languagedescription',
            name='countries',
            field=djorm_pgarray.fields.TextArrayField(dbtype='text'),
            preserve_default=True,
        ),
    ]
