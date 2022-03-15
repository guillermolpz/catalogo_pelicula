import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title('Catalogo de Peliculas')
    #root.iconbitmap('img/logo.ico')
    #En windows
    root.iconbitmap('C:\\Users\\PC\\Documents\\Desarrollo de cursos\\Python\\08 - Proyecto\\catalogo_pelicula\\catalogo-peliculas\\img\\logo.ico')
    #root.iconbitmap(r'img/logo.ico') #Icono de la ventana
   
    #frame = tk.Frame(root)
    #frame.pack()
    #frame.config(width= 480, height= 320)
    barra_menu(root = root)
    
    app = Frame(root = root)
    
    # start the program
    #root.mainloop()
    app.mainloop()
    
if __name__ == '__main__':
    main()