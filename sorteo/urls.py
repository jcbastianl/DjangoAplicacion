"""
URL configuration for sorteo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from configuraciones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('Equipo', views.Registrate, name='Registrate'),
    path('Informacion', views.Informacion, name='Informacion'),
    path('Fechas', views.Fechas, name='Fechas'),
    path('', views.Inicio, name='Inicio'),
    path('Contacto', views.Contacto, name='Contacto'),
    path('Login', views.Login, name='Login'),
    path('logout', views.logout_view, name='logout'),
    path('Enfrentamiento', views.EnfrentamientoForm, name='Enfrentamiento'),
    # path('equipo/crear', views.crear, name='crear'),
    #  path('equipo/editar', views.editar, name='editar'),
    # path('equipo/registrar', views.registrar, name='registrar'),

]
