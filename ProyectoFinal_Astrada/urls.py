"""
URL configuration for ProyectoFinal_Astrada project.

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
from django.contrib import admin
from django.urls import path
from F1app.views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('login/', LoginPagina.as_view(), name='login'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('logout/', LogoutView.as_view(template_name='F1App/logout.html'), name='logout'),
    path('acercaDeMi/', views.about, name='acerca_de_mi'),

    #URLs de los modelos creados
    path("pilotos/", ver_piloto, name="Pilotos"),
    path("equipos/", ver_equipo, name="Escuderias"),
    path("circuitos/", ver_circuito, name="Grandes Premios"),

    #URLs para crear nuevos datos
    path("nuevoPiloto/", agregar_piloto, name="Nuevo Piloto"),
    path("nuevoEquipo/", agregar_equipo, name="Nuevo Equipo"),
    path("nuevoCircuito/", agregar_circuito, name="Nuevo Circuito"),

    #URLs para actualizar 
    path("actualizarPiloto/<piloto_nombre>", actualizar_piloto, name="Actualizar Piloto"),
    path("actualizarEquipo/<equipo_nombre>", actualizar_equipo, name="Actualizar Equipo"),
    path("actualizarCircuito/<circuito_nombre>", actualizar_circuito, name="Actualizar Circuito"),

    #URLs para eliminar
    path("eliminarPiloto/<piloto_nombre>", eliminar_piloto, name="Eliminar Piloto"),
    path("eliminarEquipo/<equipo_nombre>", eliminar_equipo, name="Eliminar Equipo"),
    path("eliminarCircuito/<circuito_nombre>", eliminar_circuito, name="Eliminar Circuito"),


    #URSl para buscar
    path("buscarPilotos/", busqueda_piloto_pais, name= "Buscar Pilotos"),
    path("resultadosPilotos/", resultados_buscar_piloto_pais, name= "Resultado Pilotos"),
    path("buscarEquipos/", busqueda_equipo_pais, name= "Buscar Equipos"),
    path("resultadosEquipos/", resultados_buscar_equipo_pais, name= "Resultado Equipos"),
    path("buscarCircuitos/", busqueda_circuito_pais, name= "Buscar Circuitos"),
    path("resultadosCircuitos/", resultados_buscar_circuito_pais, name= "Resultado Circuitos"),

    #URLs para ver detalle 
    path('pilotoDetalle/<int:pk>/', PilotoDetalle.as_view(), name='piloto'),
    path('equipoDetalle/<int:pk>/', EquipoDetalle.as_view(), name='equipo'),
    path('circuitoDetalle/<int:pk>/', CircuitoDetalle.as_view(), name='circuito'),

    path('NuevoF2', F2View.as_view(), name='F2'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)