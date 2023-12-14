# financiamiento_app/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('registrar_venta/', views.registrar_venta, name='registrar_venta'),
    path('registrar_proveedor/', views.registrar_proveedor, name='registrar_proveedor'),
    path('listar_por_id/<str:model_name>/<int:id>/', views.listar_por_id, name='listar_por_id'),
    path('modificar_cliente/<int:id>/', views.modificar_cliente, name='modificar_cliente'),
    path('modificar_proveedor/<int:id>/', views.modificar_proveedor, name='modificar_proveedor'),
    path('listar_ventas_por_fechas/', views.listar_ventas_por_fechas, name='listar_ventas_por_fechas'),
]


urlpatterns += [
    path('', views.vista_raiz, name='vista_raiz'),
]

