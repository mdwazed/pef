# Generated by Django 2.1.5 on 2019-03-01 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0010_haus_display_nr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aussenanlagern',
            old_name='dacchaufbau_tiefgarage_park_wegefkache',
            new_name='dachaufbau_tiefgarage_park_wegefkache',
        ),
        migrations.RenameField(
            model_name='schlosser',
            old_name='wohnungtuer',
            new_name='wohnungstuer',
        ),
        migrations.RemoveField(
            model_name='schliessanlage',
            name='innenbaenke',
        ),
        migrations.AlterField(
            model_name='haus',
            name='aufzug',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='siteman.Aufzug'),
        ),
    ]
