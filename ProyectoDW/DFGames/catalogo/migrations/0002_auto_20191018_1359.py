# Generated by Django 2.2.6 on 2019-10-18 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name', 'fecha_creacion']},
        ),
        migrations.RenameField(
            model_name='company',
            old_name='fecha_lanzamiento',
            new_name='fecha_creacion',
        ),
    ]
