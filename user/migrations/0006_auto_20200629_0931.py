# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-29 04:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200628_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='skin',
            new_name='logotype',
        ),
        migrations.AlterField(
            model_name='temp_user',
            name='delete_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 9, 31, 33, 20089)),
        ),
    ]