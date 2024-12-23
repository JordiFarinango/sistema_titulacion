from django import forms

from .models import Empresa, Cliente, Categoria, Marca, Producto, Proveedor, Factura, Linea_de_factura

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre', 'direccion','contacto','ruc']
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cedula','nombres','apellidos','direccion',
                  'celular', 'correo'
                  ]