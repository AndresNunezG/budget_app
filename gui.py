from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msbx
from operations import *
from budget import *

class interfaz:
    def __init__(self):
        self.title = 'Budget'
        self.geometry = '710x410'
        self.resizable = False 
        self.categorias = {}

    def configurar_ventana(self):
        ventana = Tk()
        self.str_categoria_a = StringVar()
        self.str_categoria_b = StringVar()
        self.str_categoria_a.set('Seleccione')
        self.str_categoria_b.set('Seleccione')
        self.str_categoria_a.trace('w', self.opcion_selecc)
        self.str_categoria_b.trace('w', self.opcion_selecc)
        ventana.title(self.title)
        ventana.geometry(self.geometry)
        if not self.resizable:
            ventana.resizable(0, 0)
        else:
            ventana.resizable(1, 1)
        self.ventana = ventana
    
    def opcion_selecc(self, *args):
        print(self.str_categoria_a.get())

    def configurar_categorias(self):
        marco_categorias = Frame(self.ventana)
        marco_categorias.grid(columnspan=2, padx=30, pady=10)
        Label(marco_categorias, text='Categoría').grid(row=0, sticky=W)
        #self.cat_a = StringVar()
        #self.cat_a.set('Seleccione - Categoría A')
        self.dplist_a = OptionMenu(marco_categorias, self.str_categoria_a, (), command=self.crear_categoria)
        self.dplist_a.config(width=25)
        self.dplist_a.grid(row=1, pady=5)
        self.label_b = Label(marco_categorias, text='Categoría destino')
        self.label_b.grid(row=2, sticky=W)
        #self.cat_b = StringVar()
        #self.cat_b.set('Seleccione - Categoría B')
        self.dplist_b = OptionMenu(marco_categorias, self.str_categoria_b, ())
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
            value=1,
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
        marco_registros.grid(row = 0, column=2, rowspan=10, columnspan=2, padx=10, pady=30)
        tabla_registros = ttk.Treeview(marco_registros, height=14)
        tabla_registros['columns'] = ('Categoría', 'Cantidad', 'Descripción')
        tabla_registros.column('#0', width=0, stretch=NO)
        tabla_registros.column('Categoría', anchor=W, width=110)
        tabla_registros.column('Cantidad', anchor=W, width=110)
        tabla_registros.column('Descripción', anchor=W, width=110)
        tabla_registros.heading('#0', text='', anchor=W)
        tabla_registros.heading('Categoría', text='Categoría', anchor=W)
        tabla_registros.heading('Cantidad', text='Cantidad', anchor=W)
        tabla_registros.heading('Descripción', text='Descripcion', anchor=W)
        tabla_registros.pack()
    
    def configurar_crear_categoria(self):
        marco_crear_cat = Frame(self.ventana)
        marco_crear_cat.grid(column = 0, columnspan=2, padx=10, pady=10)
        Label(marco_crear_cat, text='Crear Categoría').grid(sticky=W)
        self.nueva_cat = StringVar()
        Entry(marco_crear_cat, textvariable=self.nueva_cat).grid(row=1, column=0, sticky=W)
        Button(marco_crear_cat,
            text='Crear',
            command= self.crear_categoria,
            ).grid(row=1, column=1, sticky=N)

    def configurar_enviar(self):
        marco_enviar = Frame(self.ventana)
        marco_enviar.grid(columnspan=2)
        Button(marco_enviar,
            text='Hecho',
            command=lambda:[self.recuperar_datos()],
            width=18
            ).grid(row=0, column=0, sticky=W)
    
    def recuperar_datos(self):
        #obtener los campos del formulario
        self.categoria_a = self.str_categoria_a.get()
        self.categoria_b = self.str_categoria_b.get()
        self.cantidad = float(self.amount.get())
        self.descripcion = self.description.get()
        self.operacion = self.opcion.get()
        #limpiar campos
        self.amount.set('')
        self.description.set('')
        #llamada a operations.py realizar operacion()
        btn_operacion = realizar_operacion(
            self.operacion,
            self.cantidad,
            self.descripcion,
            self.categoria_a,
            self.categoria_b,
            self.categorias)
        if btn_operacion == 'catg_igual':
            self.mensaje_alerta(alerta=btn_operacion)
        if btn_operacion is False:
            self.mensaje_alerta(alerta=btn_operacion)
        if btn_operacion:
            self.mensaje_alerta(alerta=btn_operacion)
    
    def crear_categoria(self):
        self.nueva_categoria = self.nueva_cat.get()
        self.nueva_cat.set('') #borrar campo
        #agregar objeto categoria al diccionario con nombre como llave
        if self.nueva_categoria != '' and self.nueva_categoria not in list(self.categorias.keys()):
            self.categorias[self.nueva_categoria] = categoria(self.nueva_categoria)
        #actualizar las listas desplegables de categorias
        menu_a = self.dplist_a['menu']
        menu_b = self.dplist_b['menu']
        menu_a.delete(0, 'end')
        menu_b.delete(0, 'end')
        for catg in list(self.categorias.keys()):
            menu_a.add_command(label=catg, command=lambda value=catg: self.str_categoria_a.set(catg))
            menu_b.add_command(label=catg, command=lambda value=catg: self.str_categoria_b.set(catg))

    def mensaje_alerta(self, alerta):
        if alerta == 'catg_igual':
            msbx.showwarning('Operación rechazada', 'Transferencia entre categorías iguales')
        if alerta is False:
            msbx.showwarning('Operación rechazada', 'Fondos insuficientes')
        if alerta is True:
            msbx.showinfo('Operación Exitosa', 'Deposito realizado con exito')

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
    ventana.configurar_crear_categoria()
    ventana.ejecutar_ventana()