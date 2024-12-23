from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    contacto = models.CharField(max_length=25)
    ruc = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} - {self.direccion} - {self.contacto}"

class Cliente(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=100)
    direccion = models.TextField()
    celular = models.CharField(max_length=20)
    correo = models.EmailField()
    creado_en = models.DateTimeField(auto_now_add=True, null=True)
    actualizado_en = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.cedula}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos', null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='productos', null=True, blank=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True, null=True)
    actualizado_en = models.DateTimeField(auto_now=True, null=True)

    def clean(self):
        if self.stock < 0:
            raise ValidationError("El stock no puede ser negativo.")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.nombre} {self.precio}"

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    celular = models.CharField(max_length=20)
    ruc = models.CharField(max_length=13, null=True, blank=True)
    marcas = models.ManyToManyField(Marca, related_name='proveedores')

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return f"{self.nombre} - {self.ruc or self.ruc}"

class Factura(models.Model):
    ESTADOS = [
        ('pending', 'Pendiente'),
        ('paid', 'Pagado')
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='facturas')
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pending')
    fecha = models.DateField(default=datetime.date.today)
    creado_en = models.DateTimeField(auto_now_add=True, null=True)
    actualizado_en = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self):
        return f"Orden de {self.cliente.nombres} ({self.estado})"

    def calcular_monto_total(self):
        self.monto_total = sum(linea.sub_total for linea in self.lineas.all())
       # self.save()
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.calcular_monto_total()
        super().save(*args, **kwargs)
        
class Linea_de_factura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='lineas')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    
    def calcular_sub_total(self):
        self.sub_total = self.producto.precio * self.cantidad
        

    def save(self, *args, **kwargs):
        self.calcular_sub_total()
        super().save(*args, **kwargs)
        self.factura.save()
        
    
    class Meta:
        verbose_name = "Línea de factura"
        verbose_name_plural = "Líneas de factura"
        
        
        
        
        
        
"""@receiver(pre_save, sender=Linea_de_factura)
def calcular_subtotal(sender, instance, **kwargs):
    # Solo calculamos el sub_total si no se ha guardado previamente
    if instance.sub_total == 0:
        instance.calcular_sub_total()

# Señal para actualizar el monto total de la factura cuando se guarda una línea de factura
@receiver(pre_save, sender=Linea_de_factura)
def actualizar_monto_total(sender, instance, **kwargs):
    # Verificar que no se dispare la señal recursivamente
    if not hasattr(instance, '_updating_monto_total'):
        instance._updating_monto_total = True
        instance.factura.calcular_monto_total()
        del instance._updating_monto_total"""

"""
class Cuota(models.Model):
    orden = models.ForeignKey('Orden', on_delete=models.CASCADE, related_name='cuotas')
    fecha = models.DateField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Cuota"
        verbose_name_plural = "Cuotas"

    def save(self, *args, **kwargs):
        if self.monto > self.orden.monto_restante:
            raise ValueError("El monto de la cuota no puede exceder el monto restante.")
        super().save(*args, **kwargs)
        self.orden.monto_restante -= self.monto
        self.orden.calcular_totales()

    def __str__(self):
        return f"Cuota de {self.monto} para la orden de {self.orden.cliente.nombres}"

"""