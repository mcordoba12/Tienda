from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "CategoriaProducto"
        verbose_name_plural = "CategoriasProductos"

    def __str__(self):
        return self.nombre
    
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="productos", null=True, blank=True)
    disponibilidad = models.BooleanField(default=True)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
