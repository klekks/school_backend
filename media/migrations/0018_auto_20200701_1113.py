# Generated by Django 2.2.4 on 2020-07-01 06:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0017_auto_20200701_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 11, 13, 26, 166458)),
        ),
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 11, 13, 26, 164458)),
        ),
        migrations.AlterField(
            model_name='skin',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 11, 13, 26, 166458)),
        ),
        migrations.AlterField(
            model_name='wallpaper',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 11, 13, 26, 165458)),
        ),
    ]
