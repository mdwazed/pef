# Generated by Django 2.1.5 on 2019-03-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0024_rohbau_grundung'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice_fields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=50)),
                ('option_type', models.CharField(choices=[('', '-----select-----'), ('gw', 'gewerk'), ('st', 'status'), ('gr', 'grundung')], max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.RemoveField(
            model_name='rohbau',
            name='bodenplatte',
        ),
    ]
