# Generated by Django 2.1.5 on 2019-02-26 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0007_auto_20190225_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='aussenanlagern',
            name='dacchaufbau_tiefgarage_park_wegefkache',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aussenanlagern',
            name='dachaufbau_tiefgarage_grundflache',
            field=models.TextField(blank=True, null=True),
        ),
    ]
