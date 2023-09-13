# from django.contrib.auth.forms import AuthenticationForm
from multiprocessing import AuthenticationError
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsuarioLoginForm, UsuarioRegistroForm

# Create your views here.

def index(request):
    return render(request, 'inicio.html')

def clases(request):
    return render(request, 'clases.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso.')
            return redirect('inicio')
        else:
            messages.error(request, 'Error en el formulario.')
    else:
        form = UsuarioRegistroForm()
    return render(request, 'registro_usuario.html', {'form':form})

def login_usuario(request):
    if request.method == 'POST':
        form = UsuarioLoginForm(request, data=request.POST)
        if form.is_valid():
            correo = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=correo, password=password)
            messages.success(request, 'Inicio de sesión correcta.')

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                form.add_error(None, 'Credenciales incorrectas. Por favor, inténtalo de nuevo.')
    else:
        form = UsuarioLoginForm()

    return render(request, 'login_usuario.html', {'form': form})

def logout_usuario(request):
    logout(request)
    messages.success(request, 'Sesión finalizada.')
    return redirect('inicio')