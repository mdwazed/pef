# Generated by Django 2.1.5 on 2019-04-03 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0055_turen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schlosser',
            name='eingangstuer',
        ),
        migrations.RemoveField(
            model_name='schlosser',
            name='innentueren',
        ),
        migrations.RemoveField(
            model_name='schlosser',
            name='wohnungstuer',
        ),
    ]
