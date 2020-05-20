# Generated by Django 3.0.3 on 2020-04-23 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20200423_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='time',
            new_name='start_time',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='running_time',
        ),
        migrations.AddField(
            model_name='schedule',
            name='finish_time',
            field=models.DateTimeField(null=True),
        ),
    ]
