# Generated by Django 2.2.4 on 2020-06-30 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0008_auto_20200630_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 15, 22, 59, 573995)),
        ),
    ]
