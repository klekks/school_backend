# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-29 20:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_auto_20200629_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 1, 36, 41, 744542)),
        ),
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 1, 36, 41, 743545)),
        ),
        migrations.AlterField(
            model_name='skin',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 1, 36, 41, 744542)),
        ),
        migrations.AlterField(
            model_name='wallpaper',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 1, 36, 41, 744542)),
        ),
    ]
