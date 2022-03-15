# Aplicacion de escritorio en python (Catalogo de peliculas)
_En este proyecto se creo un ejemplo sencillo de una aplicacion de escritorio en python utilizando sqlite3 para la gestion de un catalogo de peliculas._

## Comenzando
_Este proyecto es un ejemplo de como trabajar aplicaciones de escritorio en Python._

### Pre-requisitos 📋
_Para poder ejecutar la aplicación será necesario realizar los siguientes paso desde el cmd o terminal en linux_
_Crear un entorno virtual en Python_
```
Python 3.10 en windows
py -m venv env
Versiones anteriores a 3.10 de python o en linux
python -m venv env
```
_Activar el entorno virtual que se creo._
```
Windows
env\Scripts\activate.bat
Linux
source env/Scripts/activate
```
_Instalar las dependencias sobre el entorno virtual._
```
pip install numpy
pip install pyinstaller
```

### Instalación 🔧
_Para ejecutar la aplicacin corremos el siguiente comando con nuestro ambiente virtual activado._
```
Version 3.10 de python
py catalogo-peliculas\catalogo_peliculas.py
Versiones anteriores de python
python catalogo-peliculas\catalogo_peliculas.py 
```
_Al ejcutar el programa, se abrira la aplicacion como se muestra a continuacion._
![Screenshot](img.png)

## Generar ejecutable 📦
_A continuación, mostraremos como generar el ejecutable de la aplicación._
_Ya que la aplicación no es un ejemplo tan sencillo y se compone de diferentes paquetes es necesario crear un archivo spec para poder crear el ejecutable, el archivo ya esta creado, pero dejo la línea que se ejecuta para crear este archivo._
```
pyi-makespec catalogo-peliculas\catalogo_peliculas.py --windowed
```
_En este archivo se editaron las siguientes líneas para que se genere en el ejecutable la dirección a logo y a la base de datos._
```
Originalmente se verá así
datas=[],
Se pasa a esta forma
datas=[('./img/*.ico', 'img'),('./database/*.db', 'database')],
```
_Por ultimo ahora ejecutamos el archivo creado para lograr que se genere el ejecutable._
```
pyinstaller catalogo_peliculas.spec
```

_Una vez que se ejecute la sentencia anterior se crearan las siguientes carpetas build y dist, en dist encontrar una carpeta con el nombre catalogo_peliculas y dentro de esta carpeta está el ejecutable con el mismo nombre._
