from django.shortcuts import render, redirect,get_object_or_404
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


from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def index(request):
    # STock mayor a 0 
    productos = Producto.objects.filter(stock__gt=0)
    context = {'productos':productos}
    return render(request, "index.html",context)

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

@user_passes_test(lambda u:u.is_superuser,login_url=('iniciarsesion')) 
def crear_producto(request):
    if request.method == 'POST':
        producto = Producto()
        producto.nombreProducto =  request.POST.get('nombre_producto')
        producto.precio =  request.POST.get('precio_producto')
        producto.stock =  request.POST.get('stock_producto')
        producto.descripcion =  request.POST.get('descripcion_producto')
        producto.imagen =  request.FILES.get('imagen_producto')
        if request.FILES.get('imagen_producto') == None:
            # messages.error(request,'Verifique los campos porfavor')
            print('ERRORRR ')
            return redirect(request.resolver_match.url_name)
        try:
            print('PRODUCTO CREADO')
            producto.save()
            messages.success(request,'Producto creado con exito!!')
            return redirect(request.resolver_match.url_name)
        except Exception as err:
            print(err)
            messages.error(request,'No se pudo crear el producto')
            return redirect(request.resolver_match.url_name)
      
    return render(request,'crear_producto.html')

@user_passes_test(lambda u:u.is_superuser,login_url=('iniciarsesion')) 
def modificar_producto(request,id):

    producto_principal = get_object_or_404(Producto,id=id)
    if request.method == 'POST':
        producto = Producto()
        producto.id = request.POST.get('id_producto')
        producto.nombreProducto =  request.POST.get('nombre_producto')
        producto.precio =  request.POST.get('precio_producto')
        producto.stock =  request.POST.get('stock_producto')
        producto.descripcion =  request.POST.get('descripcion_producto')
   
        if request.FILES.get('imagen_producto') == None:
            producto.imagen =  producto_principal.imagen
            
         
        else:
            producto.imagen = request.FILES.get('imagen_producto')
   

            
        try:
        
            producto.save()
            messages.success(request,'Producto modifcado con exito!!')
            return redirect(request.resolver_match.url_name,id=id)
        except Exception as err:
            messages.error(request,'No se pudo crear el producto')
            print(err)
            return redirect(request.resolver_match.url_name,id=o)

    context = {'producto':producto_principal}

    return render(request,'modificar_producto.html',context)

def detalle_producto(request,id):
    producto = get_object_or_404(Producto,id=id)

    context = {'producto':producto}

    return render(request,'detalle_producto.html',context)

@user_passes_test(lambda u:u.is_superuser,login_url=('iniciarsesion')) 
def eliminar_producto(request,id):
    producto = get_object_or_404(Producto,id=id)
    try:
        producto.delete()
        messages.success(request,'Producto eliminado con exito!!!')
    except Exception as err:
        print('Error',err)
        messages.error(request,'No se pudo eliminar el producto')

    return redirect('index')

