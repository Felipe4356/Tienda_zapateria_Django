import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tiendaproject.settings')
django.setup()

from mytienda.models import CarritoProducto, Product

# Encuentra todos los CarritoProducto con producto_id no existente en Product
carrito_productos = CarritoProducto.objects.filter(producto_id__isnull=True)

# Elimina esos registros
carrito_productos.delete()

print("Datos problemáticos eliminados.")
