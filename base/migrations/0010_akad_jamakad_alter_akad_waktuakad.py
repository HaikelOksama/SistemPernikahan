# Generated by Django 4.0.8 on 2022-11-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_akad_walinikah'),
    ]

    operations = [
        migrations.AddField(
            model_name='akad',
            name='jamAkad',
            field=models.TimeField(default=None),
        ),
        migrations.AlterField(
            model_name='akad',
            name='waktuAkad',
            field=models.DateField(),
        ),
    ]
