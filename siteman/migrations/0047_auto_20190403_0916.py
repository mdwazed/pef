# Generated by Django 2.1.5 on 2019-04-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0046_sanitaer'),
    ]

    operations = [
        migrations.AddField(
            model_name='innenputz',
            name='innenputz_treppenhausdecken',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='innenputz',
            name='innenputz_treppenhauswande',
            field=models.TextField(blank=True, null=True),
        ),
    ]
