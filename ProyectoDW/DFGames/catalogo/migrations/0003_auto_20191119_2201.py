# Generated by Django 2.2.7 on 2019-11-20 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20191018_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='company',
            name='fecha_creacion',
        ),
    ]
