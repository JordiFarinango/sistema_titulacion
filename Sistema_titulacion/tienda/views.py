from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime
from .models import Empresa, Cliente, Categoria, Marca, Producto, Proveedor, Factura, Linea_de_factura
from .forms import EmpresaForm,ClienteForm

@login_required

def crear_empresa(request):
    """
    Vista para insertar los datos de la empresa
    """
    if request.method == 'POST':
        empresa_form = EmpresaForm(request.POST, request.FILES)
        
        if empresa_form.is_valid():
            empresa = empresa_form.save(commit=False)
            empresa.save()         
    else:
        empresa_form = EmpresaForm()
    
    contexto = {
        'empresa_form': empresa_form
    }        
    
    return render(request, 'base.html', contexto)     


def nuevo_cliente(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        direccion = request.POST.get('direccion')
        celular = request.POST.get('celular')
        correo = request.POST.get('correo')

        Cliente.objects.create(
            cedula=cedula,
            nombres=nombres,
            apellidos=apellidos,
            direccion=direccion,
            celular=celular,
            correo=correo
        )
        return redirect('nuevo_cliente')
    return render(request, 'nuevo_cliente.html')

def nueva_factura(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        estado = request.POST.get('estado')
        fecha = request.POST.get('fecha')
        
        cliente = Cliente.objects.get(id=cliente_id)
        
        Factura.objects.create(
            cliente=cliente,
            estado=estado,
            fecha=fecha
        )

        return redirect('nueva_factura')

    clientes = Cliente.objects.all()
    fecha_hoy = datetime.date.today()
    context = {
        'clientes': clientes,
        'fecha_hoy': fecha_hoy
    }

    return render(request, 'nueva_factura.html', context)

def nueva_linea_factura(request):
    if request.method == 'POST':
        factura_id = request.POST.get('factura')
        producto_id = request.POST.get('producto')
        cantidad = request.POST.get('cantidad')

        factura = Factura.objects.get(id=factura_id)
        producto = Producto.objects.get(id=producto_id)

        Linea_de_factura.objects.create(
            factura=factura,
            producto=producto,
            cantidad=cantidad
        )
        return redirect('nueva_linea_factura')

    facturas = Factura.objects.all()
    productos = Producto.objects.all()
    context = {
        'facturas': facturas,
        'productos': productos
    }
    return render(request, 'linea_factura.html', context)

def nuevo_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        stock = request.POST.get('stock')
        categoria_id = request.POST.get('categoria')  
        marca_id = request.POST.get('marca')  
        imagen = request.FILES.get('imagen')  
        
        categoria = Categoria.objects.get(id=categoria_id) if categoria_id else None
        marca = Marca.objects.get(id=marca_id) if marca_id else None
        
        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            stock=stock,
            categoria=categoria,
            marca=marca,
            imagen=imagen
        )

        return redirect('nuevo_producto')

    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    context = {
        'categorias': categorias,
        'marcas': marcas
    }

    return render(request, 'nuevo_producto.html', context)

def nueva_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
    
        Categoria.objects.create(nombre=nombre)

        return redirect('nueva_categoria')

    return render(request, 'nueva_categoria.html')

def nueva_marca(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        
        Marca.objects.create(nombre=nombre)

        return redirect('nueva_marca')

    return render(request, 'nueva_marca.html')

def nuevo_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        celular = request.POST.get('celular')
        ruc = request.POST.get('ruc')
        marcas_ids = request.POST.getlist('marcas')  
        
        proveedor = Proveedor.objects.create(
            nombre=nombre,
            direccion=direccion,
            celular=celular,
            ruc=ruc
        )

        if marcas_ids:
            proveedor.marcas.set(marcas_ids)

        return redirect('nuevo_proveedor')

    marcas = Marca.objects.all()
    context = {
        'marcas': marcas
    }

    return render(request, 'nuevo_proveedor.html', context)

def nueva_empresa(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        contacto = request.POST.get('contacto')
        ruc = request.POST.get('ruc')
        
        Empresa.objects.create(
            nombre=nombre,
            direccion=direccion,
            contacto=contacto,
            ruc=ruc
        )

        return redirect('nueva_empresa')

    return render(request, 'nueva_empresa.html')