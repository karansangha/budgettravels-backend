# Generated by Django 2.0.2 on 2018-02-18 02:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20180218_0105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='time',
            new_name='endTime',
        ),
        migrations.AddField(
            model_name='time',
            name='startTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
