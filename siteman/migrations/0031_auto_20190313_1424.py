# Generated by Django 2.1.5 on 2019-03-13 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0030_auto_20190313_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='dach',
            name='flchdach_stahlbeton',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dach',
            name='zeigeldach',
            field=models.TextField(blank=True, null=True),
        ),
    ]
