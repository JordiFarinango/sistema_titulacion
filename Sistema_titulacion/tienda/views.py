from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Modelos
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
    return render(request, 'nuevo_cliente.html')

def nueva_factura(request):
    return render(request, 'nueva factura.html')

def nueva_linea_factura (request):
    return render(request, 'linea_factura.html')

def nuevo_producto(request):
    return render(request, 'nuevo_producto.html')

def nueva_categoria(request):
    return render(request, 'nueva_empresa.html')

def nueva_marca(request):
    return render(request, "nueva_marca.html")

def nuevo_proveedor(request):
    return render(request, 'nuevo_proveedor.html')

def nueva_empresa(request):
    return render(request, 'nueva_empresa.html')