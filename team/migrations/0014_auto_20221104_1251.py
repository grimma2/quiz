# Generated by Django 3.2 on 2022-11-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0013_alter_team_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='bonus_points',
            field=models.PositiveIntegerField(default=0, verbose_name='Баллы команды'),
        ),
        migrations.AlterField(
            model_name='team',
            name='code',
            field=models.CharField(default='9O1DF', max_length=5, unique=True, verbose_name='Код вступления в команду'),
        ),
    ]
