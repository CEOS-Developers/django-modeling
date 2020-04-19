# Generated by Django 3.0.5 on 2020-04-19 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='myuser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.MyUser', verbose_name='유저'),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(default='', verbose_name='글내용'),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='글제목'),
        ),
    ]
