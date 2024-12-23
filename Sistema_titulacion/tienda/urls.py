from django.urls import path

from .views import crear_empresa, nuevo_cliente, nueva_factura, nueva_linea_factura, nuevo_producto, nueva_categoria, nueva_marca, nueva_empresa, nuevo_proveedor

urlpatterns = [
    path('dashboard/crear/', crear_empresa, name="crear_empresa"),

    path('nuevo_cliente', nuevo_cliente, name="nuevo_cliente"),
    path('nueva_factura', nueva_factura, name="nueva_factura"),
    path('linea_factura', nueva_linea_factura, name="linea_factura"),
    path('nuevo_producto', nuevo_producto, name="nuevo_producto"),
    path('nueva_categoria', nueva_categoria, name="nueva_categoria"),
    path('nueva_marca', nueva_marca, name="nueva_marca"),
    path('nueva_empresa', nueva_empresa, name="nueva_empresa"),
    path('nuevo_proveedor', nuevo_proveedor, name="nuevo_proveedor")

]