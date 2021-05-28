from gui import interfaz
from budget import categoria

if __name__ == '__main__':
    ventana = interfaz()
    ventana.configurar_ventana()
    ventana.configurar_categorias()
    ventana.configurar_campos()
    ventana.configurar_operacion()
    ventana.configurar_enviar()
    ventana.configurar_area()
    ventana.ejecutar_ventana()