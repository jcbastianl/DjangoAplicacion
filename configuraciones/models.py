import enum
from django.db import models

# Create your models here.


class Ligas(models.Model):
    MODO_INDIVIDUAL = 'individual'
    MODO_GRUPAL = 'grupal'

    MODO_CHOICES = (
        (MODO_INDIVIDUAL, 'Modo Individual'),
        (MODO_GRUPAL, 'Modo Grupal'),
    )

    nombre = models.CharField(max_length=50)
    modo = models.CharField(
        max_length=10,
        choices=MODO_CHOICES,
        default=MODO_INDIVIDUAL,
    )

    def __str__(self):
        return self.nombre


class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    ligas = models.ForeignKey('Ligas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Jugadores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    camiseta = models.IntegerField()
    edad = models.IntegerField()
    posicion = models.CharField(max_length=50)
    equipo = models.ForeignKey('equipo', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre



class Equipos_Registrados(models.Model):
    equipo_list = models.ManyToManyField(Equipo, related_name="equipos_inscritos")
    jugadores_list = models.ManyToManyField(Jugadores, related_name="registro_inscritos")

    def __str__(self):
        return self.nombre


class Enfrentamiento(models.Model):
    equipo1 = models.ForeignKey('equipo', on_delete=models.CASCADE, related_name="equipo1")
    equipo2 = models.ForeignKey('equipo', on_delete=models.CASCADE, related_name="equipo2")
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=50)

    def __str__(self):
        return self.equipo1.nombre + " vs " + self.equipo2.nombre
