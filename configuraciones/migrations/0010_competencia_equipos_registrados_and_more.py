# Generated by Django 4.2.3 on 2023-07-31 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuraciones', '0009_jugadores_camiseta'),
    ]

    operations = [
        migrations.CreateModel(
            name='competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='equipos_Registrados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo_list', models.ManyToManyField(related_name='equipos_inscritos', to='configuraciones.equipo')),
                ('jugadores_list', models.ManyToManyField(related_name='registro_inscritos', to='configuraciones.jugadores')),
            ],
        ),
        migrations.DeleteModel(
            name='enfrentamientoJugadores',
        ),
    ]
