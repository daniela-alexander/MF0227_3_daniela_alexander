# Sistema de Gestión de Incidencias Técnicas (HelpDesk)

## Descripción de la Arquitectura
Este proyecto integra tres unidades formativas (UF):
- **UF2404 (POO):** Modelado independiente en `core_modelos.py` aplicando encapsulamiento, herencia, polimorfismo y excepciones personalizadas.
- **UF2405 (Django & ORM):** Aplicación web desarrollada con Django, conectando modelos relacionales (Técnico e Incidencia), panel de administración personalizado y vistas basadas en clases con formularios web estilizados con Bootstrap.
- **UF2406 (Ciclo de Vida):** Control de versiones estructurado mediante Git (ramas y commits atómicos), gestión de dependencias y documentación.

## Instrucciones de Instalación y Despliegue Local

1. Clonar el repositorio y acceder a la carpeta del proyecto.

   ```bash
    git clone <URL_DEL_REPOSITORIO>
   ````

2. Crear y activar el entorno virtual:

   ```bash

   python -m venv venv

   # En Windows: venv\Scripts\activate | En Mac/Linux: source venv/bin/activate
   ```

3. Instalar dependencias:

   ```bash

   pip install -r requirements.txt

    ```

4. Configurar la base de datos y aplicar migraciones:

    ```bash

   python manage.py migrate

   ```

5. Crear un superusuario para acceder al panel de administración:
   
   ```bash

   python manage.py createsuperuser

   ```

6. Ejecutar el servidor de desarrollo:
   
   ```bash

   python manage.py runserver
   ```
   
