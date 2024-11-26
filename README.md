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

# Uso de la API REST

La API REST implementada en esta tienda en línea permite una comunicación eficiente entre el cliente (navegador o aplicación móvil) y el servidor, utilizando un conjunto de especificaciones estándar. Este diseño garantiza que las acciones necesarias para operar la tienda, como navegar por los productos, realizar compras o gestionar usuarios, sean rápidas y seguras.

## Componentes Clave de la API REST

### Verbos HTTP

Los verbos HTTP determinan la acción que el cliente desea realizar sobre los recursos disponibles. Los principales verbos utilizados son:

- **GET**: Leer información (consultar productos, obtener historial de compras, etc.).
- **POST**: Crear un nuevo recurso (registro de usuarios, creación de pedidos).
- **PUT**: Modificar un recurso existente (actualizar datos del perfil, editar carritos).
- **DELETE**: Eliminar un recurso (borrar productos del carrito).

### Dirección Única (URI)

Cada procedimiento de la API tiene una URI única que representa el recurso con el que se desea interactuar. Ejemplo:

- `/api/products/` para listar productos.
- `/api/orders/` para realizar un pedido.
- `/api/cart/` para gestionar el carrito.

### Datos Requeridos

Las solicitudes pueden incluir datos adicionales (en formato JSON) que el servidor necesita para completar la acción. Ejemplo:

- Al crear un pedido (`POST /api/orders/`), se debe enviar un objeto con los productos seleccionados y la información del usuario.

### Autenticación

Para garantizar la seguridad, muchas rutas de la API requieren autenticación basada en **JSON Web Tokens (JWT)**. Esto implica:

1. **Inicio de sesión**: El cliente envía credenciales al servidor.
2. **Token JWT**: El servidor responde con un token que el cliente debe incluir en los encabezados de futuras solicitudes.

## Flujo de Interacción Cliente-Servidor

### Cliente

El cliente es cualquier aplicación o navegador que interactúa con la tienda web, solicitando datos o enviando información a través de la API REST. Ejemplo:

- Consultar productos disponibles.
- Agregar productos al carrito.
- Finalizar una compra.

### Servidor

El servidor es quien maneja la lógica del negocio, procesa las solicitudes del cliente y responde adecuadamente. Ejemplo:

- Verificar la disponibilidad de productos en inventario.
- Procesar pedidos y registrar las transacciones en la base de datos.

