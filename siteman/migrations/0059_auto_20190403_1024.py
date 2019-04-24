# Generated by Django 2.1.5 on 2019-04-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0058_auto_20190403_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aussenanlagern',
            name='dachaufbau_tiefgarage_grundflache',
        ),
        migrations.RemoveField(
            model_name='aussenanlagern',
            name='dachaufbau_tiefgarage_park_wegeflache',
        ),
        migrations.RemoveField(
            model_name='aussenanlagern',
            name='grundflache',
        ),
        migrations.RemoveField(
            model_name='aussenanlagern',
            name='pflanzen',
        ),
        migrations.AddField(
            model_name='aussenanlagern',
            name='dachaufbau_tiefgarage_befestigt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aussenanlagern',
            name='dachaufbau_tiefgarage_grun',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aussenanlagern',
            name='feuerwehraufstellflachen',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aussenanlagern',
            name='vegetationsflachen',
            field=models.TextField(blank=True, null=True),
        ),
    ]