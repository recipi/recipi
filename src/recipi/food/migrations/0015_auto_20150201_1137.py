# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0014_auto_20150131_1958'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='weight',
            unique_together=set([('food', 'sequence')]),
        ),
    ]
