# Generated by Django 2.0.2 on 2018-04-12 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20180406_0238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelticket',
            name='hotel_city',
        ),
        migrations.RemoveField(
            model_name='hoteluserdata',
            name='hotel_ticket_city',
        ),
    ]
