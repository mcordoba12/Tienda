# Tienda en Línea 

## Integrantes:

* Juliana Filigrana Valencia
* Angela María Gonzalez Cordoba
* Fabio Felipe Rivas Murillo

## Descripción

Este proyecto consiste en el desarrollo de una tienda en línea para una empresa local, implementado con **Django Channels** para manejar comunicación en tiempo real y características estándar de comercio electrónico.

El sistema incluye roles de **administrador** y **cliente**, donde los administradores pueden gestionar el inventario y los clientes pueden realizar compras, ver facturas generadas automáticamente y consultar su historial de compras.

La solución utiliza **Django Channels** para manejar la arquitectura **ASGI**, lo que habilita capacidades avanzadas como WebSockets y un servidor robusto basado en Daphne.

---

## Características

1. **Roles de Usuario**:
   - **Administrador**:
     - Inicia sesión y gestiona productos (agregar, editar, eliminar).
   - **Cliente**:
     - Registra una cuenta, inicia sesión y navega por productos.
     - Realiza compras con generación automática de facturas.
     - Consulta su historial de compras.

2. **Persistencia de Datos**:
   - Base de datos SQLite integrada para usuarios, productos y pedidos.

3. **Seguridad**:
   - Autenticación basada en JWT para proteger rutas sensibles.

4. **Django Channels**:
   - Comunicación en tiempo real y arquitectura ASGI para manejar eventos concurrentes.

5. **APIs REST**:
   - Endpoints expuestos para gestionar usuarios, productos, carritos y pedidos.

6. **Frontend Dinámico**:
   - Interfaz responsiva utilizando Bootstrap, interactuando con el backend mediante `fetch`.

---

## Tecnologías Utilizadas

- **Backend**:
  - Django y Django REST Framework
  - Django Channels para soporte ASGI
  - JWT para autenticación segura
- **Frontend**:
  - HTML5, CSS3, JavaScript
  - Bootstrap 4
- **Servidor**:
  - Daphne
- **Base de Datos**:
  - SQLite

---

## **Requisitos Previos**
1. **Python 3.x** instalado en tu sistema.  
2. Administrador de paquetes `pip`.  
3. **Git** para clonar el repositorio.  
4. Virtualenv para crear entornos virtuales.  

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/mcordoba12/Tienda.git
   
2. Navega al directorio del proyecto:
   ```bash
    cd ProyectoWeb
   
3. Crea un entorno virtual e instala las dependencias:
   ```bash
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    pip install -r requirements.txt
   
4. Configura la base de datos y los archivos estáticos:
   ```bash
    python manage.py migrate
    python manage.py collectstatic --noinput
  
5. Ejecuta el servidor utilizando Daphne:
   ```bash
    daphne -p 9000 ProyectoWeb.asgi:application

6. Accede a la tienda en http://127.0.0.1:9000.

7. o accede simolemente con
   ```bash
    python manage.py runserver
    
8. Uso de WebSockets
Django Channels habilita la comunicación en tiempo real en la aplicación. Daphne es el servidor ASGI encargado de manejar estas conexiones. Asegúrate de que los consumidores (consumers.py) estén correctamente configurados para manejar eventos relacionados con WebSockets, como actualizaciones del carrito en tiempo real o notificaciones de pedidos.
