# Generated by Django 2.2.4 on 2020-06-30 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0011_auto_20200630_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 15, 19, 55, 650475)),
        ),
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 15, 19, 55, 649475)),
        ),
        migrations.AlterField(
            model_name='skin',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 15, 19, 55, 650475)),
        ),
        migrations.AlterField(
            model_name='wallpaper',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 15, 19, 55, 649475)),
        ),
    ]
