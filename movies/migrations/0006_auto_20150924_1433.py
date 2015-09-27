# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20150924_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movielist',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movielist',
            name='musicdirector',
        ),
    ]
