# Tarea 1: Taller de implementación de una conexión básica entre el modelo relacional y MVC utilizando SQL

**Docente:** MSc. Josselyn Tatiana Gómez

## Descripción del Proyecto

Este proyecto implementa una aplicación web utilizando el framework Django que demuestra la conexión entre el Modelo Relacional y el patrón de arquitectura MVC mediante SQL. La aplicación gestiona una biblioteca básica con autores y libros.

## Tecnologías Utilizadas

- **Framework:** Django 5.2
- **Base de Datos:** PostgreSQL 15
- **Contenedores:** Docker y Docker Compose
- **Lenguaje:** Python

## Estructura del Proyecto

```
taller-mvc-sql/
├── config/                 # Configuración del proyecto Django
│   ├── settings.py         # Configuraciones generales
│   ├── urls.py             # URLs del proyecto
│   └── wsgi.py             # Configuración para despliegue
├── core/                   # Aplicación principal
│   ├── models.py           # Modelos de datos (Author, Book)
│   ├── views.py            # Vistas para operaciones CRUD
│   ├── urls.py             # URLs de la aplicación
│   ├── forms.py            # Formularios para la creación/edición
│   └── templates/          # Plantillas HTML
│       └── core/           # Plantillas específicas de la aplicación
├── docker-compose.yml      # Configuración de Docker
└── manage.py               # Script de gestión de Django
```

## Modelos de Datos

El proyecto implementa dos modelos principales:

1. **Author (Autor)**

   - name: Nombre del autor
   - nationality: Nacionalidad del autor

2. **Book (Libro)**
   - title: Título del libro
   - publication_date: Fecha de publicación
   - author: Relación con el modelo Author (clave foránea)

## Funcionalidades

La aplicación implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para ambos modelos:

- **Autores**

  - Listado de autores
  - Detalle de autor
  - Creación de autores
  - Actualización de autores
  - Eliminación de autores

- **Libros**
  - Listado de libros
  - Detalle de libro
  - Creación de libros
  - Actualización de libros
  - Eliminación de libros

## Configuración de la Base de Datos

La aplicación utiliza PostgreSQL como sistema de gestión de base de datos relacional:

```yaml
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "db-name",
        "USER": "db-user",
        "PASSWORD": "db-password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

## Instalación y Ejecución

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/LuisRoft/taller-mvc-django.git
   cd taller-mvc-sql
   ```

2. **Configurar variables de entorno (.env)**

   Crear un archivo .env basado en el archivo .env.example y configurar las variables segun se necesite

3. **Iniciar la base de datos con Docker**

   ```bash
   docker-compose up -d
   ```

4. **Crear un entorno virtual (recomendado)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

5. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

6. **Aplicar migraciones**

   ```bash
   python manage.py migrate
   ```

7. **Iniciar el servidor de desarrollo**

   ```bash
   python manage.py runserver
   ```

8. **Acceder a la aplicación**
   - Abrir el navegador en http://localhost:8000/

## Implementación del Patrón MVC

En Django, el patrón MVC se implementa como:

- **Modelo (M):** Definido en `models.py`, representa la estructura de datos y la lógica de negocio
- **Vista (V):** Representado por las plantillas HTML en la carpeta `templates/`
- **Controlador (C):** Implementado en `views.py`, maneja las solicitudes HTTP y la lógica de la aplicación

## Relación con SQL

Django utiliza su ORM (Object-Relational Mapping) para traducir las operaciones de Python a consultas SQL. La configuración en `settings.py` establece la conexión con PostgreSQL, permitiendo que las operaciones CRUD se traduzcan a SQL.
