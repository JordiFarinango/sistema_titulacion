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