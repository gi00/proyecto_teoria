import tkinter as tk
from interfaz.gui_app import Frame, barra_menu


def main():
    root =tk.Tk()
    root.title('Proyecto De Teoría de la Simulación')
    root.iconbitmap('..\\simulador\\img\\logo.ico')
    root.geometry("800x670")
    barra_menu(root)
    
    app= Frame(root = root)
    
   
    
    
    app.mainloop() #final ejecucion

if __name__== '__main__':
    main()