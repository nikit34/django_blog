# Generated by Django 3.1 on 2020-08-24 15:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='timeStamp',
            new_name='time_stamp',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
