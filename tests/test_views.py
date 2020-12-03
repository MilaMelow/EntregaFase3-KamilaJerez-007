from django.test import TestCase, Cliente
from django.urls import reverse
from budget.models import Producto, Categoria 


class TestViews(TestCase)

    def test_project_list_GET(self):
        producto = Producto()
        response = producto.get(reverse('list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'listado_productos.htm')  
        