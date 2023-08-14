from django.contrib import admin

# Register your models here.
from .models import Equipo, Jugadores, Enfrentamiento, Ligas, Equipos_Registrados


class JugadoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'camiseta', 'edad', 'posicion', 'equipo')
    search_fields = ('nombre', 'apellido', 'camiseta', 'edad', 'posicion', 'equipo')
    list_filter = ('nombre', 'apellido', 'camiseta', 'edad', 'posicion', 'equipo')


class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ligas')
    search_fields = ('nombre', 'ligas')
    list_filter = ('nombre', 'ligas')


admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugadores, JugadoresAdmin)
admin.site.register(Enfrentamiento)
admin.site.register(Ligas)
admin.site.register(Equipos_Registrados)
