from django.db import models

# Create your models here.
#modelo para clientes
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    
# modelo para proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)


# modelo para ventas
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #primaria
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)#primaria
    fecha_venta = models.DateField()
    monto_venta = models.DecimalField(max_digits=12, decimal_places=2)
    vehiculo_adquirido = models.CharField(max_length=255)


