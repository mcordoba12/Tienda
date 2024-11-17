# models.py

from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import Sum, F


User = get_user_model()
class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']

    def __str__(self):
        return str(self.id)  # Asegúrate de devolver el ID como una cadena

    @property
    def total(self):
        # Usa el related_name 'lineas_pedido' en lugar de 'lineapedido_set'
        return self.lineas_pedido.aggregate(total=Sum(F('cantidad') * F('producto__precio')))['total'] or 0
    
class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='lineas_pedido', on_delete=models.CASCADE)  # Usar related_name para acceder a las líneas desde el pedido
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'lineas_pedidos'
        verbose_name = 'Linea de Pedido'
        verbose_name_plural = 'Lineas de Pedidos'
        ordering = ['id']

    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre}'

