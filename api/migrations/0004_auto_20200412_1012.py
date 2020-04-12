# Generated by Django 3.0.5 on 2020-04-12 01:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200412_0948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'ordering': ('-transport',), 'verbose_name': '배송', 'verbose_name_plural': '배송들'},
        ),
        migrations.AlterField(
            model_name='delivery',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order', verbose_name='주문식별'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_num', models.AutoField(primary_key=True, serialize=False, verbose_name='글번호 PK')),
                ('title', models.CharField(max_length=100, verbose_name='글제목')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='글사진')),
                ('content', models.TextField(verbose_name='글내용')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성일자')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order', verbose_name='주문식별')),
            ],
        ),
    ]
