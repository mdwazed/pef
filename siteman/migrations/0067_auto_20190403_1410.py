# Generated by Django 2.1.5 on 2019-04-03 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0066_auto_20190403_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='innenputz',
            name='edelputz_bad',
        ),
        migrations.RemoveField(
            model_name='innenputz',
            name='edelputz_wohnraume',
        ),
    ]