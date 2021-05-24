from tkinter import *

class interfaz:
    def __init__(self):
        self.title = 'Budget'
        self.geometry = '300x450'
        self.resizable = False

    def configurar_ventana(self):
        ventana = Tk()
        ventana.title(self.title)
        ventana.geometry(self.geometry)
        if not self.resizable:
            ventana.resizable(0, 0)
        else:
            ventana.resizable(1, 1)
        self.ventana = ventana

    def ejecutar_ventana(self):
        self.ventana.mainloop()

def configurar_categorias(ventana):
    marco_categorias = Frame(ventana.ventana)
    marco_categorias.grid(columnspan=3, padx=20, pady=10)
    Label(marco_categorias, text = 'Origen: ').grid(row=0, column=0)
    Entry(marco_categorias).grid(row=0, column= 1, columnspan=2)
    Label(marco_categorias, text = 'Destino: ').grid(row=1, column=0)
    Entry(marco_categorias).grid(row=1, column= 1, columnspan=2)

def configurar_operacion(ventana):
    operacion = ''
    def operacion_seleccionada():
        operacion = opcion.get()
    marco_operacion = Frame(ventana.ventana)
    marco_operacion.grid()
    opcion = StringVar()
    Radiobutton(
        marco_operacion,
        text='Deposito',
        value='Deposito',
        variable=opcion,
        command=operacion_seleccionada
        ).grid(row=0, sticky=W)
    Radiobutton(
        marco_operacion,
        text='Retiro',
        value='Retiro',
        variable=opcion,
        command=operacion_seleccionada
        ).grid(row=1, sticky=W)
    Radiobutton(
        marco_operacion,
        text='Transferencia',
        value='Transferencia',
        variable=opcion,
        command=operacion_seleccionada
        ).grid(row=2, sticky=W)
    return opcion

if __name__ == '__main__':
    ventana = interfaz()
    ventana.configurar_ventana()
    configurar_categorias(ventana)
    configurar_operacion(ventana)
    ventana.ejecutar_ventana()