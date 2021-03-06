# Aplicacion de escritorio en python (Catalogo de peliculas)
_En este proyecto se creo un ejemplo sencillo de una aplicacion de escritorio en python utilizando sqlite3 para la gestion de un catalogo de peliculas._

## Comenzando
_Este proyecto es un ejemplo de como trabajar aplicaciones de escritorio en Python._

### Pre-requisitos 馃搵
_Para poder ejecutar la aplicaci贸n ser谩 necesario realizar los siguientes paso desde el cmd o terminal en linux_
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

### Instalaci贸n 馃敡
_Para ejecutar la aplicacin corremos el siguiente comando con nuestro ambiente virtual activado._
```
Version 3.10 de python
py catalogo-peliculas\catalogo_peliculas.py
Versiones anteriores de python
python catalogo-peliculas\catalogo_peliculas.py 
```
_Al ejcutar el programa, se abrira la aplicacion como se muestra a continuacion._
<img src="img.PNG" alt="Imagen de la palicaci贸n"/>

## Generar ejecutable 馃摝
_A continuaci贸n, mostraremos como generar el ejecutable de la aplicaci贸n._
_Ya que la aplicaci贸n no es un ejemplo tan sencillo y se compone de diferentes paquetes es necesario crear un archivo spec para poder crear el ejecutable, el archivo ya esta creado, pero dejo la l铆nea que se ejecuta para crear este archivo._
```
pyi-makespec catalogo-peliculas\catalogo_peliculas.py --windowed
```
_En este archivo se editaron las siguientes l铆neas para que se genere en el ejecutable la direcci贸n a logo y a la base de datos._
```
Originalmente se ver谩 as铆
datas=[],
Se pasa a esta forma
datas=[('./img/*.ico', 'img'),('./database/*.db', 'database')],
```
_Por ultimo ahora ejecutamos el archivo creado para lograr que se genere el ejecutable._
```
pyinstaller catalogo_peliculas.spec
```

_Una vez que se ejecute la sentencia anterior se crearan las siguientes carpetas build y dist, en dist encontrar una carpeta con el nombre catalogo_peliculas y dentro de esta carpeta est谩 el ejecutable con el mismo nombre._
