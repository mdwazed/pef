# Generated by Django 2.1.5 on 2019-03-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0033_fenster_algemeine_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='fenster',
            name='beschattung',
            field=models.TextField(blank=True, null=True),
        ),
    ]
