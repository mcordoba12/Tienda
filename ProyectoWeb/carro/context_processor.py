def importe_total_carro(request):
    total = 0 #inicializamos la variable global total
    if request.user.is_authenticated: #si el usuario esta autenticado
        for key, value in request.session["carro"].items(): #recorremos el carro
            total = total + float(value["precio"]) * value["cantidad"] #calculamos el importe total del carro
            
    else:
        total = "Debes iniciar sesión" #si el usuario no esta autenticado, mostramos un mensaje
    return {"importe_total_carro":total} #retornamos el importe total del carro