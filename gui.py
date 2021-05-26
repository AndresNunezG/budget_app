from tkinter import *

class interfaz:
    def __init__(self):
        self.title = 'Budget'
        self.geometry = '350x450'
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

    def configurar_categorias(self):
        marco_categorias = Frame(self.ventana)
        marco_categorias.grid(columnspan=2, padx=30, pady=10)
        self.cat_a = StringVar()
        self.cat_a.set('Seleccione - Categoría A')
        dplist_a = OptionMenu(marco_categorias, self.cat_a, 'Seleccione')
        dplist_a.config(width=25)
        dplist_a.grid(row=0, pady=5)
        self.cat_b = StringVar()
        self.cat_b.set('Seleccione - Categoría B')
        self.dplist_b = OptionMenu(marco_categorias, self.cat_b, 'Seleccione')
        self.dplist_b.config(width=25)
        self.dplist_b.grid(row=1, pady=5)

    def configurar_campos(self):
        marco_campos = Frame(self.ventana)
        marco_campos.grid(columnspan=2, padx=30, pady=10)
        self.amount = StringVar()
        Label(marco_campos, text='Cantidad').grid(row=0, column=0, sticky=W)
        Entry(marco_campos, textvariable = self.amount).grid(row=0, column=1)
        self.description = StringVar()
        Label(marco_campos, text='Descripción').grid(row=1, column=0)
        Entry(marco_campos, textvariable = self.description).grid(row=1, column=1)

    def configurar_operacion(self):
        marco_operacion = Frame(self.ventana)
        marco_operacion.grid(columnspan=1, padx=25, pady=10, sticky=W)
        self.opcion = IntVar()
        def operacion_seleccionada():
            self.opcion.get()
            if self.opcion.get() == 3:
                self.dplist_b.config(state='active')
            else:
                self.dplist_b.config(state='disabled')
        Radiobutton(
            marco_operacion,
            text='Deposito',
            value= 1,
            variable=self.opcion,
            command=operacion_seleccionada
            ).grid(row=0, sticky=W)
        Radiobutton(
            marco_operacion,
            text='Retiro',
            value=2,
            variable=self.opcion,
            command=operacion_seleccionada
            ).grid(row=1, sticky=W)
        Radiobutton(
            marco_operacion,
            text='Transferencia',
            value=3,
            variable=self.opcion,
            command=operacion_seleccionada
            ).grid(row=2, sticky=W)
    
    def configurar_enviar(self):
        marco_enviar = Frame(self.ventana)
        marco_enviar.grid(columnspan=2)
        Button(marco_enviar, text='Enviar', command=self.recuperar_datos).grid(row=0, column=1)
    
    def recuperar_datos(self):
        return (
            self.cat_a.get(),
            self.cat_b.get(),
            self.amount.get(),
            self.description.get(),
            self.opcion.get()
            )

    def ejecutar_ventana(self):
        self.ventana.mainloop()

if __name__ == '__main__':
    ventana = interfaz()
    ventana.configurar_ventana()
    ventana.configurar_categorias()
    ventana.configurar_campos()
    ventana.configurar_operacion()
    ventana.configurar_enviar()
    ventana.ejecutar_ventana()