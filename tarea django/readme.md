Pasos para inciar el proyecto, se penso el proyecto para una tienda de videojuegos, con 5 aplicaciones y 3 modelos cada una 

Se necesita tener instalado python y se debera realizar todo el proceso en un entorno virtual 

todo se debe trabajar en la carpeta donde esten las aplicaciones 

python -m venv venv para #para crear el entorno virtual 

venv\Scripts\Activate.ps1 #para iniciar el entorno virtual 
(venv) debera aparecer al inicio de la ruta que estamos trabajando 

Dentro del entorno virtual 
pip install django #para instalar django

python manage.py migrate #para que se realizen las migraciones de las aplicaciones que tiene el proyecto 

python manage.py showmigrations # para revisar que se realizaron todas las migraciones 

python manage.py createsuperuser #para crear un admin para tener acceso a las aplicaciones, corre opcional y contraseña obligatorio

python manage.py runserver #para iniciar el proyecto el cual estara alojado en 
http://127.0.0.0.1:8000/admin/

ahi vera que estaran las aplicaciones creadas 


deactivate #para salirse del entorno virtual 

