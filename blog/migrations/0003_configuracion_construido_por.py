# Generated by Django 4.1.2 on 2022-10-23 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_configuarcion_configuracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='construido_por',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
