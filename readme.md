# Budget App with TKinter and Python 馃枼 馃悕

### 馃挰 Feel free of do some pull requests or any kind of contribution
### Haz la contribuci贸n o pregunta que desees!

####  馃摫 馃挼 Interfaz principal  
![Transferencia](/imgs_readme/img_transferencia.png)  
####  鈩癸笍 Notificaci贸n de dep贸sito exitoso  
![Notificaci贸n dep贸sito](/imgs_readme/img_notificacion_deposito.png)  
#### 聽鈿狅笍 Error en la transferencia  
Ocasionada por falta de fondos o transferencia entre categor铆as iguales 
![Error en la transferencia](/imgs_readme/img_error_transferencia.png)  

## 馃搨 Documentos
<code>budget.py</code>  
<code>main.py</code>  
<code>gui.py</code>  

### 馃敼 budget.py
<code>class categoria</code>:  
M贸dulo con la clase **cateogoria** que cuenta con los siguientes **atributos**:
- nombre: identificado para la categor铆a y par谩metro requerido la creaci贸n de la clase
- registro: objeto de estructura [{'cantidad': ,'descripcion': }, ] para almacenar de manera vol谩til la informaci贸n hist贸rica de las transacciones realizadas en la categor铆a
**metodos**:
- deposito: agregar una cantidad positiva (+) a la categor铆a
- retiro: retirar de la categoria una cantidad (-) si la categor铆a cuenta con los fondos suficientes
- obtener_balance: devuelve el balance de todas las transacciones que se encuentren en el registro
- verificar_fondos: recibe como par谩metro una cantidad y regresa False la cantidad es mayor al balance, de lo contrario regresa True
- transferir: recibe como par谩metro una cantidad y una categoria, si se cuenta con los fondos se hace un retiro desde la categor铆a origen y se hace un deposito en la categor铆a destino. Se devuelve True si la transacci贸n fue exitosa, False de lo contrario.

### 馃敼 gui.py
<code>class interfaz</code>:  
M贸dulo con el c贸digo de la interfaz gr谩fica hecha con TKinter donde se muestra la informaci贸n de las 煤ltimas transacciones realizadas, el formulario para realizar 茅stas y la opci贸n de crear nuevas categor铆as

### 馃敼 operaciones.py
<code>def realizar_operacion</code>:  
Utiliza la clase **categoria** y la informaci贸n extra铆da del formulario para hacer la transacci贸n y hacer validaciones para mostrar alertas en caso de ser necesarias

### 馃敼 main.py
<code>if __name__ == '__main__': print('Rock it!馃幐')</code>  
Orquestador principal que llama a los m贸dulos necesarios para la ejecuci贸 principal