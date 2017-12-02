# API's con Django Rest Framework

En este proyecto se desarrollaran API's con Django Rest Framework, desde Serializadores básicos,
hasta personalización de los Seralizadores. Se utilizara el interprete de *python3*, por lo que
debemos verificar si tenemos instalada la versión, ingresando en la terminal o consola de comandos.
Se utilizara como gestor de bases de datos a MySQL,
se requieren instalar las siguientes apps:
```
pip3 install Django==1.11.7
pip3 install djangorestframework==3.7.3
pip3 install django-filter==1.1.0
pip3 install mysqlclient==1.3.12
```

Los pasos a tener en cuenta son los sigueintes:
1. Crear un base de datos con el nombre **rest_db**.
2. Agregar las credenciales en el archivo *settings.py* de la configuración de tu servidor de bases de datos:
```[python]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rest_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': your_number_port
    }
}
```
3. Correr la app en el servidor local:
```
python3 manage.py runserver
```