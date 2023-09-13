from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from .forms import UsuarioLoginForm

urlpatterns = [
    path('inicio/', views.index, name='inicio'),
    path('clases/', views.clases, name='clases'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout')
]