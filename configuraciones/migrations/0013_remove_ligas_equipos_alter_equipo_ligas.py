# Generated by Django 4.2.3 on 2023-08-01 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuraciones', '0012_ligas_equipos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ligas',
            name='equipos',
        ),
        migrations.AlterField(
            model_name='equipo',
            name='ligas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='configuraciones.ligas'),
            preserve_default=False,
        ),
    ]
