# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20150924_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='director',
            field=models.CharField(default=None, max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='musicdirector',
            field=models.CharField(default=None, max_length=200, blank=True),
        ),
    ]
