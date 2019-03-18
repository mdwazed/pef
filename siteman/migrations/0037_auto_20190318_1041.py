# Generated by Django 2.1.5 on 2019-03-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0036_auto_20190318_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='aussenanlagern',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aussenputz',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bodenbelaege',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dach',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='elektro',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='erdbau',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='estrich',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fenster',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fliesenleger',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='innenputz',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='maler',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='raumbuch_elektro',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rohbau',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sanitaer',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schliessanlage',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schlosser',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schreiner',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sicherheitstechnik',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trockenbau',
            name='sonstiges',
            field=models.TextField(blank=True, null=True),
        ),
    ]
