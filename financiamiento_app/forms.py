# financiamientos_app/forms.py
from django import forms
from .models import Cliente, Proveedor, Venta

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'proveedor', 'fecha_venta', 'monto_venta', 'vehiculo_adquirido']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre']
