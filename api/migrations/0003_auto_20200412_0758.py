# Generated by Django 3.0.5 on 2020-04-11 22:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200412_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.CharField(max_length=100, null=True, verbose_name='destination'),
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='pro_num',
        ),
        migrations.AddField(
            model_name='myuser',
            name='pro_num',
            field=models.ManyToManyField(through='api.Order', to='api.Product', verbose_name='number of product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date ordered'),
        ),
    ]
