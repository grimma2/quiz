# Generated by Django 3.2 on 2022-11-05 06:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_auto_20221105_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finishteam',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 5, 6, 17, 1, 482871, tzinfo=utc), verbose_name='Дата и время финиша команды'),
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 5, 6, 17, 1, 482871, tzinfo=utc), verbose_name='Дата начала игры'),
        ),
    ]
