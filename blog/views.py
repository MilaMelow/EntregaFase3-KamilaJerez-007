from django.shortcuts import render, redirect
from .models import *
from .forms import  ContactoForm, ProductoForm, CreateUserForm
from django import forms
from django.forms import ModelForm

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required(login_url='iniciarsesion')

def productos(request):
    productos = Producto.objects.all()
    return render(request, "productos.html", {"listaProductos":productos})

def estilo(request):
    return render(request, 'estilo.html', {})


def accesorios(request):
    return render(request, 'accesorios.html', {})


def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado"
        else:
            data["form"] = formulario

    return render(request, 'contacto.html', data)



def registrar(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'La cueta fue creada por ' + user)

                return redirect('iniciarsesion')


        context = {'form':form}
        return render(request, 'registrar.html', context)


def iniciarsesion(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'El nombre de usuario o contraseñas son incorrectos :c')

        context = {}
        return render(request, 'iniciarsesion.html', context)

def cerrarsesion(request):
    logout(request)
    return redirect ('iniciarsesion')

@login_required(login_url='iniciarsesion')


def listado_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    
    return render(request, 'listado_productos.html', data)


def nuevo_producto(request):
    data = {
        'form': ProductoForm()
    }
    return render(request, 'nuevo_producto.html', data)



def buscar_producto(request):
    return render(request, "buscar_producto.html")

def buscar(request):

    if request.GET["prd"]:

        #mensaje="Producto encontrado: %r" %request.GET ["prd"] 
        producto=request.GET["prd"]
            
        productos=Producto.objects.filter(nombreProducto__icontains=producto)

        return render(request, "resultados_busqueda.html", {"productos":productos, "query":producto})

    else:

        mensaje="No hay información disponible de este producto :("


        return HttpResponse(mensaje)


def tienda(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda.html', context)

