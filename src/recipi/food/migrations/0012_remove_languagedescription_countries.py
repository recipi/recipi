# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_languagedescription_countries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languagedescription',
            name='countries',
        ),
    ]
