from django import forms
from django.forms import ModelForm
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'


class ProductoForm(forms.ModelForm):

        model = Producto    
        fields = '__all__'


