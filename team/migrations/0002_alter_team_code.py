# Generated by Django 3.2 on 2022-12-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='code',
            field=models.CharField(default='9Q.G.', max_length=5, unique=True, verbose_name='Код вступления в команду'),
        ),
    ]
