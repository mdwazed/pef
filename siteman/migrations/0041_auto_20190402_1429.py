# Generated by Django 2.1.5 on 2019-04-02 14:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0040_wohnungplan'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice_options',
        ),
        migrations.RenameField(
            model_name='dach',
            old_name='dach',
            new_name='hauptdach',
        ),
        migrations.RemoveField(
            model_name='rohbau',
            name='dach',
        ),
        migrations.RemoveField(
            model_name='rohbau',
            name='installationschachte',
        ),
        migrations.AddField(
            model_name='dach',
            name='dachterrassen',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dach',
            name='spenglerarbeiten',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rohbau',
            name='horizontale_abdichtung',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rohbau',
            name='vertikale_abdictung',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rohbau',
            name='wohnungstrenwande',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='plan',
            field=models.FileField(blank=True, null=True, upload_to='haus/plan_pdf/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg'])]),
        ),
        migrations.AlterField(
            model_name='wohnungplan',
            name='components',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='wohnungplan',
            name='plan',
            field=models.FileField(blank=True, null=True, upload_to='wohnung/plan_pdf/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg'])]),
        ),
    ]