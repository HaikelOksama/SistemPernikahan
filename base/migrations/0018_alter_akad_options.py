# Generated by Django 4.0.8 on 2022-11-29 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_akad_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='akad',
            options={'ordering': ['-created']},
        ),
    ]