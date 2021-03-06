# Generated by Django 2.1.5 on 2019-03-18 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0034_fenster_beschattung'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicefields',
            name='option',
            field=models.CharField(default='sl', max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='choicefields',
            name='option_type',
            field=models.CharField(choices=[('sl', '--select--'), ('gw', 'gewerk'), ('st', 'status'), ('gr', 'grundung'), ('aw_eg_og_dg', 'aussenwande_eg_og_dg'), ('dach', 'dach'), ('fenster_beschattung', 'fenster_beschattung')], max_length=50),
        ),
    ]
