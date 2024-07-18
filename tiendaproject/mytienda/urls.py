from django.urls import path
from .views import  agregar_al_carrito, ver_carrito, eliminar_del_carrito
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/', views.producto, name='producto'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('carrito/', login_required(ver_carrito), name='ver_carrito'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('eliminar/<int:elemento_id>/', login_required(eliminar_del_carrito), name='eliminar_del_carrito'),
    path('agregar/<int:producto_id>/', login_required(agregar_al_carrito), name='agregar_al_carrito'),
    path('contacto_nuevo/', views.contacto_nuevo, name='contacto_nuevo'),
    path('contacto/<int:pk>',views.contacto_detalle, name='contacto_detalle'),
    path('contacto/<int:pk>/editar/',views.contacto_editar, name='contacto_editar'),
    path('contacto/<int:pk>/eliminar/',views.contacto_eliminar, name='contacto_eliminar'),
    path('contactos/',views.contacto_lista, name='contacto_lista'),
    path('contacto_confirmacion/', views.contacto_confirmacion, name='contacto_confirmacion'),

    ]