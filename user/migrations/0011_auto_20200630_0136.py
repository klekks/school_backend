# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-29 20:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20200629_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp_user',
            name='delete_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 1, 36, 41, 740557)),
        ),
    ]
