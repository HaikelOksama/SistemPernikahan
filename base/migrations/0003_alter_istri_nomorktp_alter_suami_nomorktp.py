# Generated by Django 4.0.8 on 2022-11-18 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_akad_created_akad_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='istri',
            name='nomorKtp',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='suami',
            name='nomorKtp',
            field=models.CharField(max_length=16),
        ),
    ]
