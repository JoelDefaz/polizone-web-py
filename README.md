# Proyecto Polizone Web - Calidad de Software

Este proyecto está configurado para ser ejecutado en un servidor web utilizando Django. A continuación, se detallan los pasos necesarios para configurar el entorno y desplegar la aplicación.

# Configuración

## 1.Requisitos

- **IDE de Desarrollo(App desarrollada en VSC)**
- **Python** (versión 3.12.4 o superior)
- **Git** para el versionamiento de cambios

## 2.Descarga del Proyecto
### Clonar el repositorio

1. Clonar el proyecto del repositorio anfitrion: `https://github.com/JoelDefaz/polizone-web-py.git`. De no clonarlo, descargar todo el proyecto y preparalo en un ambiente y esapcio adecuado.

## 3.Configuración

Sigue los pasos a continuación para configurar el servidor en **Django**


1. En el ambiente/carpeta preparada donde se encuentra el proyecto abrir la consola para crear un ambiente en python y que asi las libreraias no sean un problema, asi que ejecutamos el siguiente comando:
```
python -m venv <Nombre del ambiente>
```
3. Una vez creado el ambiente vamos a activar el ambiente para realizar las instalaciones de las dependecias necesarias, asi que ejecutamos el siguiente comando:
comando
```
<Nombre del ambiente>/Scripts/Active
```
*Nota:Echo esto deberia mostrarse el nombre del ambiente a la derecha de la ruta actual de  trabajo*
```
(<Nombre del ambiente>) <Ruta actual de trabajo>
```
4. Activado el ambiente pasamos a instalar las dependecias necesarias, para ellos buscamos el archivo llamado **requirements.txt**, y en la consola ejecutamos el siguiente comando:
```
pip install -r <ruta>\requirements.txt 
```
5. Una vez termine de instalar las dependecias, ya se puede pasar a ejecutar el proyecto

## 4. Ejecutar el Proyecto

1. Para ejecutar el proyecto se necesita identificar el archivo **manage.py**. Una vez hecho, en la consola se ejecuta el siguiente comando:
```
python <ruta>/manage.py runserver
```
2. Asi generalmente ya se encuentra ejecutando el servidor y se podra visitar la pagina web en la direccion `http://localhost:8000/` o `http://127.0.0.1:8000/`

## Problemas con Django
Para cualquie problema relacionado con Django se puede buscar toda la documentación en: `https://docs.djangoproject.com/es/5.1/`
