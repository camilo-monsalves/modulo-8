
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Usuario
from django import forms

class UsuarioRegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['rut','nombre_completo','direccion', 'correo', 'telefono', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        custom_classes = 'w-full py-3 px-6 rounded-xl form-control'
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = custom_classes

class UsuarioLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))