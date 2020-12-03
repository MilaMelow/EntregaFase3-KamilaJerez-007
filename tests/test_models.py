from blog.models import Producto

class ProductoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Producto.objects.create(nombreProducto ='Pantalon', precio = '10000')

    def test_nombreProducto_label(self):
        producto=Producto.objects.get(id=1)
        field_label = producto._meta.get_field('nombreProducto').verbose_name
        self.assertEquals(field_label, 'nombreProducto')