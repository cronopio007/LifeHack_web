from django.shortcuts import render

#importar la mixins
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic


# Create your views here.

class Inicio(generic.TemplateView):
    template_name = 'bases/home.html'

class serv_1(generic.TemplateView):
    template_name = 'bases/servicio1.html'

class Pruebas(generic.TemplateView):
    template_name = 'bases/prueba.html'

class Porque(generic.TemplateView):
    template_name = 'bases/xqLifeHack.html'

class Servicio1(generic.TemplateView):
    template_name = 'bases/servicio1.html'

class Servicio2(generic.TemplateView):
    template_name = 'bases/servicio2.html'

class Servicio3(generic.TemplateView):
    template_name = 'bases/servicio3.html'

class Servicio4(generic.TemplateView):
    template_name = 'bases/servicio4.html'

class Servicio5(generic.TemplateView):
    template_name = 'bases/servicio5.html'

class Servicio6(generic.TemplateView):
    template_name = 'bases/servicio6.html'

class Portafolio(generic.TemplateView):
    template_name = 'bases/portafolio.html'

