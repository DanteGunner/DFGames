# Generated by Django 2.2.7 on 2019-11-20 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20191119_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='fecha_lanzamiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]