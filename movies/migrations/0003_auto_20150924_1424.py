# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20150924_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='director',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='musicdirector',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
