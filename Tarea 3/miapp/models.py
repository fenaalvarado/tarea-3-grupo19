from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField (max_length = 45)
	descripcion = models.CharField (max_length = 450)

class Producto(models.Model):
	nombre = models.CharField (max_length = 45)
	precio = models.IntegerField()
	descripcion = models.CharField (max_length = 450)
	disponibilidad = models.BooleanField(default = False)
	categoria = models.ForeignKey (Categoria, on_delete = models.CASCADE)

class Usuario(models.Model):
	nombre = models.CharField (max_length = 55)
	direccion = models.CharField (max_length = 100)
	telefono = models.CharField (max_length = 15)
	correo = models.EmailField(max_length = 254)

class Carrito(models.Model):
    monto = models.IntegerField()
    cantidad = models.IntegerField()
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)

class DetalleCompra(models.Model):
    fecha = models.DateField()
    comentario = models.CharField (max_length = 450)
    evaluacionNota = models.IntegerField()
    carrito = models.ForeignKey (Carrito, on_delete = models.CASCADE)

