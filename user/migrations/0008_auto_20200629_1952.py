# Generated by Django 2.2.4 on 2020-06-29 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200629_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp_user',
            name='delete_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 19, 52, 8, 831567)),
        ),
    ]
