# Generated by Django 2.1.5 on 2019-03-06 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0013_auto_20190301_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='architekt_plan',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
