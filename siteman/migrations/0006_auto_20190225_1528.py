# Generated by Django 2.1.5 on 2019-02-25 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0005_auto_20190225_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aussenanlagern',
            old_name='grundfladhe',
            new_name='grundflache',
        ),
    ]