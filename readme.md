# Budget App with TKinter and Python 🖥 🐍

### 💬 Feel free of do some pull requests or any kind of contribution
### Haz la contribución o pregunta que desees!

#### 📱 💵 Interfaz principal
![Transferencia](/imgs_readme/img_transferencia.png)
#### ℹ️ Notificación de depósito exitoso
![Notificación depósito](/imgs_readme/img_notificacion_deposito.png)
#### ⚠️ Error en la transferencia
Ocasionada por falta de fondos o transferencia entre categorías iguales 
![Error en la transferencia](/imgs_readme/img_error_transferencia.png)

## 📂 Documentos
<code>budget.py</code>  
<code>main.py</code>  
<code>gui.py</code>  

### 🔹 budget.py
<code>class categoria</code>:  
Módulo con la clase **cateogoria** que cuenta con los siguientes **atributos**:
- nombre: identificado para la categoría y parámetro requerido la creación de la clase
- registro: objeto de estructura [{'cantidad': ,'descripcion': }, ] para almacenar de manera volátil la información histórica de las transacciones realizadas en la categoría
**metodos**:
- deposito: agregar una cantidad positiva (+) a la categoría
- retiro: retirar de la categoria una cantidad (-) si la categoría cuenta con los fondos suficientes
- obtener_balance: devuelve el balance de todas las transacciones que se encuentren en el registro
- verificar_fondos: recibe como parámetro una cantidad y regresa False la cantidad es mayor al balance, de lo contrario regresa True
- transferir: recibe como parámetro una cantidad y una categoria, si se cuenta con los fondos se hace un retiro desde la categoría origen y se hace un deposito en la categoría destino. Se devuelve True si la transacción fue exitosa, False de lo contrario.

### 🔹 gui.py
<code>class interfaz</code>:  
Módulo con el código de la interfaz gráfica hecha con TKinter donde se muestra la información de las últimas transacciones realizadas, el formulario para realizar éstas y la opción de crear nuevas categorías

### 🔹 operaciones.py
<code>def realizar_operacion</code>:  
Utiliza la clase **categoria** y la información extraída del formulario para hacer la transacción y hacer validaciones para mostrar alertas en caso de ser necesarias

### 🔹 main.py
<code>if __name__ == '__main__': print('Rock it!🎸')</code>  
Orquestador principal que llama a los módulos necesarios para la ejecució principal