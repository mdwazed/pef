# Generated by Django 2.1.5 on 2019-04-03 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0047_auto_20190403_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estrich',
            old_name='daemmplatten',
            new_name='dammplatten',
        ),
        migrations.RemoveField(
            model_name='estrich',
            name='estrich',
        ),
    ]