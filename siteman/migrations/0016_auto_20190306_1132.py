# Generated by Django 2.1.5 on 2019-03-06 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0015_auto_20190306_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanitaer',
            name='abwasserung',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sanitaer',
            name='haus',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='siteman.Haus'),
        ),
        migrations.AddField(
            model_name='sanitaer',
            name='heizung',
            field=models.TextField(blank=True, null=True),
        ),
    ]
