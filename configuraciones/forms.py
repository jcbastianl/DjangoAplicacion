from django import forms

from .models import Ligas, Equipo, Jugadores, Enfrentamiento

class LigasForm(forms.ModelForm):
    class Meta:
        model = Ligas
        fields = ['nombre', 'modo']

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'ligas']

class JugadoresForm(forms.ModelForm):
    class Meta:
        model = Jugadores
        fields = ['nombre', 'apellido', 'camiseta', 'edad', 'posicion', 'equipo']
class EnfrentamientoForm(forms.ModelForm):
    class Meta:
        model = Enfrentamiento
        fields = ['equipo1', 'equipo2', 'fecha', 'hora', 'lugar']