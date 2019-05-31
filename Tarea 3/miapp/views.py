from django.shortcuts import render
from .models import Categoria, Usuario, Producto, Carrito, DetalleCompra
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
#from .models import Proyecto


# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')



# Carrito

def user_cart(request):
	userr = user.request
	usuario = Usuario.objects.get (user = userr)
	contexto = {"carritos": Carrito.objects.all(), "nombre": usuario.nombre, "direccion": usuario.direccion, "correo":usuario.correo, "telefono": usuario.telefono }

	return render(request, 'miapp/user_cart.html', contexto)


# Productos

def lista_productos(request):
	contexto={"productos": Producto.objects.all()}

	return render(request, 'miapp/lista_productos.html', contexto)


# Usuarios

def crear_usuario(request):
	contexto = {}
	contexto['grupos'] = Grupo.objects.all()
	return render(request, 'miapp/new_user.html', contexto)

def usuario_creado(request):
	nombre = request.POST['nombre']
	correo = request.POST['mail']
	telefono = request.POST['tel']
	direccion = request.POST['direc']

	username = request.POST['username']
	password = request.POST['password']
	user = User.objects.create_user(username=username, password=password)

	usuario = Usuario(user=user, nombre=nombre, direccion = direccion, telefono = telefono, correo=correo)
	usuario.save()

	contexto = {"username": username, "nombre": nombre, "direccion":direccion}
	return render(request, 'miapp/user_created.html', contexto)



# Entrar/Salir Cuenta

def loginView(request):
	return render(request, 'miapp/login.html')

def auth(request):
	username = request.POST['username']
	password = request.POST['password']
	usuario = authenticate(username=username, password=password)
	login(request, usuario)

	return render(request, 'miapp/index.html')

def logoutView(request):
	logout(request)
	return render(request, 'miapp/index.html')



	