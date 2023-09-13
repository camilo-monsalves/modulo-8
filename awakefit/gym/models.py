from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission, Group

# Create your models here.

class Usuario(AbstractUser):
    rut = models.CharField(max_length=12, unique=True)
    nombre_completo = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.username + " " + self.correo
    
    class Meta:
        verbose_name_plural = 'Usuarios'

    groups = models.ManyToManyField(
        Group,
        verbose_name='grupos de usuarios',
        blank=True,
        related_name='usuarios',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='permisos de usuario',
        blank=True,
        related_name='usuarios',
    )
    
class Instructor(Usuario):
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'Instructor: {self.nombre_completo}, Disponible: {self.disponible}'
    
    class Meta:
        verbose_name_plural = 'Instructores'
    
class Clase(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    horarios = models.CharField(max_length=255)
    duracion = models.PositiveIntegerField() # si la duracion de la clase se mide en minutos.
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE) # si se elimina el instructor, las clases asociadas se borraran.

class Sucursal(models.Model):
    direccion = models.CharField(max_length=100)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    servicios_adicionales = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.direccion
    
    class Meta:
        verbose_name_plural = 'Sucursales'
    
class Cliente(Usuario):
    cuota_al_dia = models.BooleanField(default=True)
    clases = models.ManyToManyField(Clase, verbose_name='Clases Cliente')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_DEFAULT, default=None ,verbose_name='Sucursal Cliente')

    def __str__(self):
        return f'Cliente: {self.nombre}, Cuota diaria: {self.cuota_diaria}'
    
    class Meta:
        verbose_name_plural = 'Clientes'
    



