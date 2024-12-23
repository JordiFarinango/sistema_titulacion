# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Empresa, Cliente, Categoria, Marca, Producto, Proveedor, Factura, Linea_de_factura


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion', 'contacto', 'ruc')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cedula',
        'nombres',
        'apellidos',
        'direccion',
        'celular',
        'correo',
        'creado_en',
        'actualizado_en',
    )
    list_filter = ('creado_en', 'actualizado_en')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creado_en')
    list_filter = ('creado_en',)


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creado_en')
    list_filter = ('creado_en',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'precio',
        'descripcion',
        'stock',
        'categoria',
        'marca',
        'imagen',
        'creado_en',
        'actualizado_en',
    )
    list_filter = ('categoria', 'marca', 'creado_en', 'actualizado_en')


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion', 'celular', 'ruc')
    raw_id_fields = ('marcas',)


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'monto_total', 'estado', 'creado_en')
    list_filter = ('cliente', 'creado_en')
    readonly_fields =['monto_total']


@admin.register(Linea_de_factura)
class Linea_de_facturaAdmin(admin.ModelAdmin):
    list_display = ('factura', 'producto', 'cantidad','sub_total')
    list_filter = ('factura', 'producto')
    readonly_fields = ['sub_total']