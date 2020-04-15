# Generated by Django 3.0.3 on 2020-04-12 05:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_seat'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='api.Schedule')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat', to='api.Seat')),
            ],
        ),
    ]
