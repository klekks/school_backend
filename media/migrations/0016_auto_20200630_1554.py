# Generated by Django 2.2.4 on 2020-06-30 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0015_auto_20200630_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 15, 54, 32, 176245)),
        ),
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 15, 54, 32, 174245)),
        ),
        migrations.AlterField(
            model_name='skin',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 15, 54, 32, 176245)),
        ),
        migrations.AlterField(
            model_name='wallpaper',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 15, 54, 32, 175245)),
        ),
    ]