# Generated by Django 2.1.5 on 2019-03-06 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0016_auto_20190306_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aussenanlagern',
            old_name='dachaufbau_tiefgarage_park_wegefkache',
            new_name='dachaufbau_tiefgarage_park_wegeflache',
        ),
    ]
