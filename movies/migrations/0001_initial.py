# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movieName', models.CharField(max_length=200)),
                ('title', models.TextField()),
                ('url', models.URLField()),
                ('views', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('hero', models.CharField(max_length=200)),
                ('heroine', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('musicdirector', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
