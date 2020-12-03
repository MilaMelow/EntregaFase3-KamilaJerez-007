from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombreProducto = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.CharField (max_length=100)
    cantidad = models.IntegerField()
    imagen = models.ImageField(null=True, upload_to='static/img/')

    def __str__(self):
        return self.name
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Pedidos(models.Model):
    idPedidos = models.IntegerField(primary_key=True)
    fechaCompra = models.DateField()
    precio = models.IntegerField()
    cantidad = models.IntegerField()

class DetallePedido (models.Model):
    idDetallePedido = models.IntegerField(primary_key=True)
    precio = models.IntegerField()
    descuento = models.IntegerField()

class Cliente (models.Model):
    idCliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correoElectronico = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    cuidad = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    codigoPostal = models.IntegerField()
    numeroTelefono = models.IntegerField()

opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"],
]


class Contacto (models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def publish(self):
                self.save()

    def __str__(self):
        return self.nombre
        
