# Generated by Django 3.2 on 2022-11-05 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0016_alter_team_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='code',
            field=models.CharField(default='Y18P_', max_length=5, unique=True, verbose_name='Код вступления в команду'),
        ),
    ]
