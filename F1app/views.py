from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.decorators import login_required
from . import views

from F1app.models import Piloto, Equipo, Circuito
from F1app.forms import PilotoFormulario, EquipoFormulario, CircuitoFormulario, RegistrarUsuario, EditarUsuario
# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'F1App/home.html'

class LoginPagina(LoginView):
    template_name = 'F1app/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')
    
    
class RegistroPagina(FormView):
    template_name = 'F1app/registro.html'
    form_class = RegistrarUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = EditarUsuario
    template_name= 'F1App/edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

#Acerca de mi
def about(request):
    return render(request, 'F1app/acercaDeMi.html', {})


#CRUD Piloto
@login_required
def agregar_piloto(request):

    if request.method == "POST":

        nuevo_formulario = PilotoFormulario(request.POST)

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data

            piloto_nuevo = Piloto(nombre=info["nombre"], nacionalidad=info["nacionalidad"], fecha_nacimiento=info["fecha_nacimiento"], puntos_totales=info["puntos_totales"])

            piloto_nuevo.save()

            return render(request, "F1app/home.html")
    
    else:

        nuevo_formulario  = PilotoFormulario() 

    return render(request, "F1app/formu_piloto.html", {"mi_formu":nuevo_formulario})

@login_required
def ver_piloto(request):

    mis_pilotos = Piloto.objects.all() 

    info = {"pilotos":mis_pilotos}

    return render(request, "F1app/pilotos.html", info)


class PilotoDetalle(LoginRequiredMixin, DetailView):
    model = Piloto
    context_object_name = 'piloto'
    template_name = 'F1app/pilotoDetalle.html'

@login_required
def actualizar_piloto(request, piloto_nombre):
    
    piloto_escogido = get_object_or_404(Piloto, pk=piloto_nombre)

    if request.method == "POST":

        nuevo_formulario = PilotoFormulario(request.POST) 

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data 

            piloto_escogido.nombre = info["nombre"]
            piloto_escogido.nacionalidad = info["nacionalidad"]
            piloto_escogido.fecha_nacimiento = info["fecha_nacimiento"]
            piloto_escogido.puntos_totales = info["puntos_totales"]

            piloto_escogido.save()

            return render(request, "F1app/home.html") 
    
    else: 

        nuevo_formulario  = PilotoFormulario(initial={"nombre": piloto_escogido.nombre,
                                                     "nacionalidad":piloto_escogido.nacionalidad,
                                                     "fecha_nacimiento":piloto_escogido.fecha_nacimiento,
                                                     "puntos_totales": piloto_escogido.puntos_totales})

    return render(request, "F1app/update_piloto.html", {"mi_formu":nuevo_formulario})

@login_required
def eliminar_piloto(request, piloto_nombre):

    piloto_escogido = get_object_or_404(Piloto, pk=piloto_nombre)

    if request.method == 'POST':
        piloto_escogido.delete()
        return render(request, "F1app/pilotos.html")

    return render(request, "F1app/confirmar_eliminacion.html", {'piloto': piloto_escogido})

@login_required
def busqueda_piloto_pais(request):

    return render(request, "F1app/buscar_piloto_pais.html")

@login_required
def resultados_buscar_piloto_pais(request):

    if request.method=="GET":

        nacionalidad_pedido = request.GET["nacionalidad"]
        resultados_pilotos = Piloto.objects.filter(nacionalidad__icontains=nacionalidad_pedido)


        return render(request, "F1app/buscar_piloto_pais.html", {"pilotos":resultados_pilotos})

    else:
        return render(request, "F1app/buscar_piloto_pais.html")
    


#CRUD Equipo
@login_required
def agregar_equipo(request):

    if request.method == "POST":

        new_formulario = EquipoFormulario(request.POST)

        if new_formulario.is_valid():

            info = new_formulario.cleaned_data

            equipo_nuevo = Equipo(nombre=info["nombre"], pais=info["pais"], fundacion=info["fundacion"], campeonatos=info["campeonatos"])

            equipo_nuevo.save()

            return render(request, "F1app/home.html")
    
    else:

        new_formulario  = EquipoFormulario() 

    return render(request, "F1app/formu_equipo.html", {"mi_formu":new_formulario})

@login_required
def ver_equipo(request):

    mis_equipos = Equipo.objects.all() 

    info = {"equipos":mis_equipos}

    return render(request, "F1app/equipos.html", info)


class EquipoDetalle(LoginRequiredMixin, DetailView):
    model = Equipo
    context_object_name = 'equipo'
    template_name = 'F1app/equipoDetalle.html'

@login_required
def actualizar_equipo(request, equipo_nombre):
    
    equipo_escogido = get_object_or_404(Equipo, pk=equipo_nombre)

    if request.method == "POST":

        nuevo_formulario = EquipoFormulario(request.POST) 

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data 

            equipo_escogido.nombre = info["nombre"]
            equipo_escogido.pais = info["pais"]
            equipo_escogido.fundacion = info["fundacion"]
            equipo_escogido.campeonatos = info["campeonatos"]

            equipo_escogido.save()

            return render(request, "F1app/home.html") 
    
    else: 

        nuevo_formulario  = EquipoFormulario(initial={"nombre": equipo_escogido.nombre,
                                                     "pais":equipo_escogido.pais,
                                                     "fundacion":equipo_escogido.fundacion,
                                                     "campeonatos": equipo_escogido.campeonatos})

    return render(request, "F1app/update_equipo.html", {"mi_formu":nuevo_formulario})

@login_required
def eliminar_equipo(request, equipo_nombre):

    equipo_escogido = get_object_or_404(Equipo, pk=equipo_nombre)

    if request.method == 'POST':
        equipo_escogido.delete()
        return render(request, "F1app/equipos.html")

    return render(request, "F1app/confirmar_eliminacion_equipo.html", {'equipo': equipo_escogido})

@login_required
def busqueda_equipo_pais(request):

    return render(request, "F1app/buscar_equipo_pais.html")

@login_required
def resultados_buscar_equipo_pais(request):

    if request.method=="GET":

        pais_pedido = request.GET["nacionalidad"]
        resultados_equipos = Equipo.objects.filter(pais__icontains=pais_pedido)


        return render(request, "F1app/buscar_equipo_pais.html", {"equipos":resultados_equipos})

    else:
        return render(request, "F1app/buscar_equipo_pais.html")


#Crud Circuito
@login_required
def agregar_circuito(request):

    if request.method == "POST":

        nuevo_formulario = CircuitoFormulario(request.POST)

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data

            circuito_nuevo = Circuito(nombre=info["nombre"], pais=info["pais"], longitud_km=info["longitud_km"], record_vuelta=info["record_vuelta"])

            circuito_nuevo.save()

            return render(request, "F1app/home.html")
    
    else:

        nuevo_formulario  = CircuitoFormulario() 

    return render(request, "F1app/formu_circuito.html", {"mi_formu":nuevo_formulario})

@login_required
def ver_circuito(request):

    mis_circuitos = Circuito.objects.all() 

    info = {"circuitos":mis_circuitos}

    return render(request, "F1app/circuitos.html", info)


class CircuitoDetalle(LoginRequiredMixin, DetailView):
    model = Circuito
    context_object_name = 'circuito'
    template_name = 'F1app/circuitoDetalle.html'

@login_required
def actualizar_circuito(request, circuito_nombre):
    
    circuito_escogido = get_object_or_404(Circuito, pk=circuito_nombre)

    if request.method == "POST":

        nuevo_formulario = CircuitoFormulario(request.POST) 

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data 

            circuito_escogido.nombre = info["nombre"]
            circuito_escogido.pais = info["pais"]
            circuito_escogido.longitud_km = info["longitud_km"]
            circuito_escogido.record_vuelta = info["record_vuelta"]

            circuito_escogido.save()

            return render(request, "F1app/home.html") 
    
    else: 

        nuevo_formulario  = CircuitoFormulario(initial={"nombre": circuito_escogido.nombre,
                                                     "pais":circuito_escogido.pais,
                                                     "longitud_km":circuito_escogido.longitud_km,
                                                     "record_vuelta": circuito_escogido.record_vuelta})

    return render(request, "F1app/update_circuito.html", {"mi_formu":nuevo_formulario})

@login_required
def eliminar_circuito(request, circuito_nombre):

    circuito_escogido = get_object_or_404(Circuito, pk=circuito_nombre)

    if request.method == 'POST':
        circuito_escogido.delete()
        return render(request, "F1app/circuitos.html")

    return render(request, "F1app/confirmar_eliminacion_circuito.html", {'circuito': circuito_escogido})

@login_required
def busqueda_circuito_pais(request):

    return render(request, "F1app/buscar_circuito_pais.html")

@login_required
def resultados_buscar_circuito_pais(request):

    if request.method=="GET":

        longitud_km_pedido = request.GET["longitud_km"]
        resultados_circuitos = Circuito.objects.filter(longitud_km__icontains=longitud_km_pedido)


        return render(request, "F1app/buscar_circuito_pais.html", {"circuitos":resultados_circuitos})

    else:
        return render(request, "F1app/buscar_circuito_pais.html")

class F2View(TemplateView):
    template_name = 'F1App/en_construccion.html'