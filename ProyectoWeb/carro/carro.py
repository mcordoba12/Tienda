class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            carro = self.session['carro'] = {}
        self.carro = carro

    def agregar(self, producto): 
        if str(producto.id) not in self.carro.keys():  # Si el producto no está en el carro
            self.carro[producto.id] = {  # Agregarlo al carro
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:  # Si el producto ya está en el carro
            self.carro[str(producto.id)]["cantidad"] += 1  # Aumentar la cantidad
            # No es necesario cambiar el precio aquí, ya que el precio se establece al agregar el producto.

        self.guardarCarro()  # Guardar el carro en la sesión


    def guardarCarro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto.id = str(producto.id)  # convertimos el id del producto a string
        if producto.id in self.carro:  # si el producto está en el carro
            del self.carro[producto.id]  # lo eliminamos
            self.guardarCarro()

    def restar_producto(self, producto):  # método para restar productos al carro
        for key, value in self.carro.items():  # recorremos el carro
            if key == str(producto.id):  # si el producto ya está en el carro
                value["cantidad"] -= 1  # restamos la cantidad del producto
                value["precio"] = str(float(value["precio"]) - producto.precio)

                if value["cantidad"] < 1:  # si la cantidad del producto es menor a 1
                    self.eliminar(producto)  # eliminamos el producto del carro   

                break
        self.guardarCarro()

    def limpiar_carro(self):  # método para limpiar el carro
        self.session["carro"] = {}  # limpiamos el carro
        self.session.modified = True  # indicamos que la sesión ha sido modificada
