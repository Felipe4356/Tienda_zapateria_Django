from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Carrito, CarritoProducto as ElementoCarrito, Contacto , Category
from .forms import CantidadProductoForm, ContactoForm,forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages






def index(request):
    productos = Product.objects.all()
    return render(request, 'index.html', {'productos': productos})

def producto(request):
    return render(request, 'producto.html')



def lista_productos(request):
    category_id = request.GET.get('category')
    
    if category_id:
        productos = Product.objects.filter(category_id=category_id)
    else:
        productos = Product.objects.all()
    categorias = Category.objects.all()
    
    return render(request, 'lista_productos.html', {
        'productos': productos,
        'categorias': categorias
    })


def detalle_producto(request, pk):
    producto = get_object_or_404(Product, pk=pk)
    return render(request, 'detalle_producto.html', {'producto': producto})


def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Product, id=producto_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        form = CantidadProductoForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
            
            if cantidad > producto.stock:
                form.add_error('cantidad', 'La cantidad solicitada excede el stock disponible.')
            else:
                elemento, creado = ElementoCarrito.objects.get_or_create(carrito=carrito, producto=producto)
                if not creado:
                    elemento.cantidad += cantidad
                else:
                    elemento.cantidad = cantidad
                elemento.save()
                return redirect('ver_carrito')
    else:
        form = CantidadProductoForm()

    return render(request, 'detalle_producto.html', {'producto': producto, 'form': form})

@login_required
def ver_carrito(request):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    elementos = ElementoCarrito.objects.filter(carrito=carrito)
    
    total_carrito = 0
    for elemento in elementos:
        elemento.total = elemento.producto.price * elemento.cantidad
        total_carrito += elemento.total
    
    return render(request, 'ver_carrito.html', {'elementos': elementos, 'total_carrito': total_carrito})

@login_required
def eliminar_del_carrito(request, elemento_id):
    elemento = get_object_or_404(ElementoCarrito, id=elemento_id)
    elemento.delete()
    return redirect('ver_carrito')




def contacto_nuevo(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_confirmacion')
    else:
        form = ContactoForm()
    return render(request, 'myportfolio/contacto_nuevo.html', {'form': form})


@login_required
def contacto_detalle(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'mytienda/contacto_detalle.html', {'contacto': contacto})

@login_required
def contacto_editar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('contacto_detalle', pk=contacto.pk)
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'mytienda/contacto_editar.html', {'form': form})

@login_required
def contacto_eliminar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return redirect('contacto_lista')

@login_required
def contacto_lista(request):
    contactos = Contacto.objects.all()
    return render(request, 'mytienda/contacto_lista.html', {'contactos': contactos})

def contacto_confirmacion(request):
    return render(request, 'mytienda/contacto_confirmacion.html')
    

