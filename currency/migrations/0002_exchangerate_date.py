# Generated by Django 3.2.15 on 2022-09-26 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangerate',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 26, 13, 13, 4, 562368), verbose_name='Date'),
        ),
    ]
