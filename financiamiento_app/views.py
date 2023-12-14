from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente,Proveedor,Venta
from django.http import HttpResponse
from . import views 
# Create your views here.

def vista_raiz(request):
    return render(request,'base.html')
    
def registrar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        cliente = Cliente.objects.create(nombre=nombre, direccion=direccion)
        return redirect ('registrar_cliente')
    
    return render(request,'registrar_cliente.html')


def registrar_venta(request):
    clientes = Cliente.objects.all()
    proveedores = Proveedor.objects.all()

    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        proveedor = request.POST.get('proveedor')
        fecha_venta = request.POST.get('fecha_venta')
        monto_venta = request.POST.get('monto_venta')
        vehiculo_adquirido = request.POST.get('vehiculo_adquirido')

        try:
            # Convierte los IDs a enteros
            cliente_id = int(cliente)
            proveedor_id = int(proveedor)

            # Obtén las instancias de Cliente y Proveedor
            cliente = get_object_or_404(Cliente, id=cliente)
            proveedor = get_object_or_404(Proveedor, id=proveedor)

            # Crea la venta con las instancias de Cliente y Proveedor
            venta = Venta.objects.create(
                cliente=cliente,
                proveedor=proveedor,
                fecha_venta=fecha_venta,
                monto_venta=monto_venta,
                vehiculo_adquirido=vehiculo_adquirido
            )

            return redirect('registrar_venta')

        except (ValueError, Cliente.DoesNotExist, Proveedor.DoesNotExist) as e:
            # Manejar la excepción adecuadamente, por ejemplo, redirigir a una página de error
            return render(request, 'error.html', {'error_message': str(e)})

    return render(request, 'registrar_venta.html', {'clientes': clientes, 'proveedores': proveedores})


    ## registar proveedor
def registrar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        proveedor = Proveedor.objects.create(nombre=nombre)
        return redirect('registrar_proveedor')

    return render(request,'registrar_proveedor.html')


## LISTAR BUSQUEDA POR ID

def listar_por_id(request,model_name,id):
    model_class = None
    if model_name == 'cliente':
        model_class = Cliente
    elif model_name == 'proveedor':
        model_class = Proveedor;
    elif model_name == 'venta':
        model_class = Venta

#error 404
    item = get_object_or_404 (model_class,id=id)
    return render(request,'listar_por_id.html',{'item': item})
## modificar datos

def modificar_cliente(request,id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.direccion = request.POST.get('direccion')
        cliente.save()
        return redirect ('modificar_cliente', id=id)
    return render (request, 'modificar_cliente.html', {'cliente':cliente})

def modificar_proveedor(request,id):
    cliente = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.save()
        return redirect ('modificar_proveedor', id=id)
    return render (request, 'modificar_proveedor.html', {'proveedor':proveedor})

# listar por fechas
def listar_ventas_por_fechas(request):
    if request.method == 'POST':
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        ventas =Venta.objects.filter(fecha_venta__range=(fecha_inicio,fecha_fin))
        return render (request, 'listar_ventas_por_fechas.html', {'ventas':ventas})
    return render(request, 'filtro_fechas.html')



