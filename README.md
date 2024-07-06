# PROYECTO FINAL DE VENTAS 

## Instalacion de dependencias
    pip install -r requirements.txt

## Pasos para conectar PostgreSQL
- Se debe instalar la versión 14 de PostgreSQL.
- Despues de realizar la instalación, se debe recordar la contraseña del usuario **postgres** que se definió.
- Se abre una terminal y se ejecuta: **psql -U postgres**
- Se coloca la contraseña, de esa manera se entra al Shell de PostgreSQL.
- Ingresar para crear la base de datos: **CREATE DATABASE "e-commerce";** 
- Salir del Shell.
- En la ruta principal del proyecto, crear un archivo *'.env'* con la siguiente estructura:<br>
    DB_ENGINE=django.db.backends.postgresql  
    DB_DATABASE=e-commerce  
    DB_USERNAME=postgres  
    DB_PASSWORD=**Contraseña aquí**  
    DB_SOCKET=localhost  
    DB_PORT=5432  
- Ejecutar las migraciones: **py manage.py migrate**

## Tailwind CSS
- Ejecutar: cd tailwind && npm run watch
- Instalar:
    npm install @tailwindcss/forms --save-dev  
    npm install @tailwindcss/typography --save-dev   
    npm install @tailwindcss/aspect-ratio --save-dev   