# Generated by Django 4.2.3 on 2023-07-30 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuraciones', '0005_remove_enfrentamientojugadores_equipo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='pais',
            new_name='liga',
        ),
    ]