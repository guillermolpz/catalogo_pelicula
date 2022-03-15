# Aplicacion de escritorio en python (Catalogo de peliculas)
_En este proyecto se creo un ejemplo sencillo de una aplicacion de escritorio en python utilizando sqlite3 para la gestion de un catalogo de peliculas._

## Comenzando
_Puede descagar el proyecto como apoyo para quienes comienzan en python._

### Pre-requisitos 📋

### Instalación 🔧

## Generar ejecutable 📦
_Acontinuación las instrucciones para generar un ejecutable._
_Ya que el ejemplo no es tan sencillo no se pude generar un ejecutable de forma rapida es necesario realizar lo siguiente._
_Instalar._
```
pip install pyinstaller
```
_Crear el archivo .spec que permitira genera el archivo ejecutable._
```
pyi-makespec catalogo_peliculas.py --windowed
```
_Una vez que se genere el archivo .spec sera neserario editarlo en la datas_
```
Originalmente se vera asi
datas=[],
Se de pasar a esta forma
datas=[('./img/*.ico', 'img'),('./database/*.db', 'database')],
```
_Por ultimo ahora ejecutamos el archivo creado para lograr que se genere el ejecutable._
```
pyinstaller catalogo_peliculas.spec
```


## Construido con 🛠️
