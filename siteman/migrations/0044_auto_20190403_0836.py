# Generated by Django 2.1.5 on 2019-04-03 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0043_remove_fenster_algemeine_information'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sanitaer',
            name='haus',
        ),
        migrations.RemoveField(
            model_name='sanitaer',
            name='wohnung',
        ),
        migrations.DeleteModel(
            name='Sanitaer',
        ),
    ]
