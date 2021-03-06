# Generated by Django 2.1.5 on 2019-03-21 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteman', '0037_auto_20190318_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('components', models.CharField(choices=[('ar', 'Architeckt'), ('eb', 'Erdbau'), ('fen', 'Fenster'), ('sla', 'Schliessanlage')], max_length=50)),
                ('plan', models.FileField(blank=True, null=True, upload_to='plan_pdf/')),
                ('haus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteman.Haus')),
            ],
        ),
    ]
