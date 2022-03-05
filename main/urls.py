from django.urls import path

#hay q importar todas las vistas para q no use el login de dj
from django.contrib.auth import  views as auth_views

#hay q importar la vista q se creo en views
from main.views import Inicio, serv_1, Pruebas, Porque, Servicio1, Servicio2, Servicio3, Servicio4, Servicio5, Servicio6, Portafolio


urlpatterns=[
    path('', Inicio.as_view(), name='Inicio'),
    path('servicio1', serv_1. as_view(), name='servicio1'),
    path('pruebas', Pruebas.as_view(), name= 'miPueba' ),
    path('xqLifeHack',Porque.as_view(),name= 'Xq'),

    # paginas de los servicios

    path('software', Servicio1.as_view(), name='software' ),
    path('web_app',Servicio2.as_view(), name="web_app"),
    path('social_media', Servicio3.as_view(), name="socialMedia"),
    path('hosting',Servicio4.as_view(), name='hosting' ),
    path('branding', Servicio5.as_view(), name="branding"),
    path('publicidad', Servicio6.as_view(), name='publicidad'),


#portafolio
    path('portafolio', Portafolio.as_view(), name="portafolio")
    
]