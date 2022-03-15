import sqlite3
from tkinter import messagebox

# Clase de conexion a la BD
class ConexionDB:
    def __init__(self):
        # Esta primera opcion se pude utilizar sin problemas en linux
        #self.base_datos = "database/peliculas.db"
        # Esta se utiliza en windows para indicar el directorio donde se encuentra la base de datos sqlite3
        self.base_datos = "C:\\Users\\PC\\Documents\Desarrollo de cursos\\Python\\08 - Proyecto\\catalogo_pelicula\\catalogo-peliculas\\database\\peliculas.db"
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
        
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()