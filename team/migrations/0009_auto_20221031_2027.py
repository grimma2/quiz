# Generated by Django 3.2 on 2022-10-31 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0008_alter_team_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(auto_now=True, verbose_name='Время отсчёта таймера вопроса')),
                ('task_id', models.CharField(max_length=99, verbose_name='id таска отвечающего за таймер')),
            ],
        ),
        migrations.AlterField(
            model_name='team',
            name='code',
            field=models.CharField(default='.X9HN', max_length=5, unique=True, verbose_name='Код вступления в команду'),
        ),
        migrations.AddField(
            model_name='team',
            name='timer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team', to='team.timer'),
        ),
    ]