# Generated by Django 4.1.2 on 2022-11-01 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0002_familiar_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='fecha_de_nacimiento',
        ),
    ]
