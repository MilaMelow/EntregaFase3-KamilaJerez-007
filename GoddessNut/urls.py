"""GoddessNut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import index, productos, contacto, crear_producto, detalle_producto, modificar_producto, eliminar_producto, registrar, listado_productos, nuevo_producto, buscar_producto
from blog.views import buscar, iniciarsesion, cerrarsesion
from django.conf.urls.static import static
from django.conf import settings

#RESTFRAMEWORK
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'usuarios', UserViewSet)

urlpatterns = [
    path('iniciarsesion/', iniciarsesion, name='iniciarsesion'),
    path('registrar/', registrar, name='registrar'),
    path('cerrarsesion/', cerrarsesion, name='cerrarsesion'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('productos/', productos, name='productos'),
    path('contacto/', contacto, name='contacto'),
    path('listado-productos/', listado_productos, name='listado_productos'),
    path('nuevo-producto/', nuevo_producto, name= 'nuevo_producto'),
    path('buscar-producto/', buscar_producto, name='buscar_producto'),
    path('buscar/', buscar, name='buscar'),
    path('crear_producto/',crear_producto,name="Crear producto"),
    path('modificar_producto/<int:id>/',modificar_producto,name="Modificar producto"),
    path('eliminar_producto/<int:id>/',eliminar_producto,name="Eliminar producto"),
    path('detalle_producto/<int:id>/',detalle_producto,name="Detalle producto"),
    path('api/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('allauth.urls')),
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
