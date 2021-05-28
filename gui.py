from tkinter import *
from tkinter import ttk
from operations import *
from budget import *

class interfaz:
    def __init__(self):
        self.title = 'Budget'
        self.geometry = '350x600'
        self.resizable = False 
        self.categorias = {}

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
        Label(marco_categorias, text='Categoría').grid(row=0, sticky=W)
        self.cat_a = StringVar()
        self.cat_a.set('Seleccione - Categoría A')
        dplist_a = OptionMenu(marco_categorias, self.cat_a, 'Seleccione', 'comida', 'servicios')
        dplist_a.config(width=25)
        dplist_a.grid(row=1, pady=5)
        self.label_b = Label(marco_categorias, text='Categoría destino')
        self.label_b.grid(row=2, sticky=W)
        self.cat_b = StringVar()
        self.cat_b.set('Seleccione - Categoría B')
        self.dplist_b = OptionMenu(marco_categorias, self.cat_b, 'Seleccione', 'comida', 'servicios')
        self.dplist_b.config(width=25)
        self.dplist_b.grid(row=3, pady=5)

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
                self.label_b.config(fg='black')
            else:
                self.dplist_b.config(state='disabled')
                self.label_b.config(fg='gray')
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

    def configurar_panel_registros(self):
        marco_registros = Frame(self.ventana)
        marco_registros.grid(columnspan=2, padx=10, pady=10)
        tabla_registros = ttk.Treeview(marco_registros)
        tabla_registros['columns'] = ('Cantidad', 'Descripción')
        tabla_registros.column('#0', width=0, stretch=NO)
        tabla_registros.column('Cantidad', anchor=W, width=145)
        tabla_registros.column('Descripción', anchor=W, width=145)
        tabla_registros.heading('#0', text='', anchor=W)
        tabla_registros.heading('Cantidad', text='Cantidad', anchor=W)
        tabla_registros.heading('Descripción', text='Descripcion', anchor=W)
        tabla_registros.pack()
    
    def configurar_crear_categoria(self):
        marco_crear_cat = Frame(self.ventana)
        marco_crear_cat.grid(columnspan=2)
        return True

    def configurar_enviar(self):
        marco_enviar = Frame(self.ventana)
        marco_enviar.grid(columnspan=2)
        Button(marco_enviar,
            text='Hecho',
            command=lambda:[self.recuperar_datos()],
            ).grid(row=0, column=1)
    
    def recuperar_datos(self):
        self.categoria_a = self.cat_a.get()
        self.categoria_b = self.cat_b.get()
        self.cantidad = float(self.amount.get())
        self.descripcion = self.description.get()
        self.operacion = self.opcion.get()
        realizar_operacion(
            self.operacion,
            self.cantidad,
            self.descripcion,
            self.categoria_a,
            self.categoria_b,
            self.categorias)

    def ejecutar_ventana(self):
        self.ventana.mainloop()

if __name__ == '__main__':
    ventana = interfaz()
    ventana.configurar_ventana()
    ventana.configurar_categorias()
    ventana.configurar_campos()
    ventana.configurar_operacion()
    ventana.configurar_enviar()
    ventana.configurar_panel_registros()
    ventana.ejecutar_ventana()