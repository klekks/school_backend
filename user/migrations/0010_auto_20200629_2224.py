# Generated by Django 2.2.4 on 2020-06-29 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200629_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp_user',
            name='delete_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 22, 23, 33, 671190)),
        ),
    ]
