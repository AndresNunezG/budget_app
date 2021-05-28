class categoria():
    def __init__(self, nombre):
        self.nombre = nombre
        self.registro = []
    
    def deposito(self, cantidad, descripcion=''):
        self.registro.append({'cantidad':cantidad, 'descripcion': descripcion})

    def retiro(self, cantidad, descripcion=''):
        if self.verificar_fondos(cantidad):
            self.registro.append({'cantidad': -1*cantidad, 'descripcion': descripcion})
            return True
        else:
            return False

    def obtener_balance(self):
        balance = 0
        for movimiento in self.registro:
            balance += movimiento['cantidad']
        return balance

    def verificar_fondos(self, cantidad):
        return False if cantidad > self.obtener_balance() else True
    
    def transferir(self, cantidad, transferir_to):
        descripcion = f'transferir to {transferir_to.nombre}'
        successful_transferir = self.retiro(cantidad, descripcion)
        if successful_transferir:
            descripcion = f'transferir from {self.nombre}'
            transferir_to.deposito(cantidad, descripcion)
            return True
        else:
            return False

if __name__ == '__main__':
    
    #crear categoria de comida y agregar depositos y retiros
    food = categoria('food')
    food.deposito(200, 'deposito 1')
    food.deposito(350, 'deposito 2')
    food.retiro(100, 'sandwich')

    #imprimir balance de la categoria comida
    print('Balance categoría food: ', end='')
    print(food.obtener_balance())

    #verificar si se cuenta con una cantidad de 400 disponible
    print('400 disponibles?: ', end='')
    print(food.verificar_fondos(400))

    #crear categoría de ropa
    clothes = categoria('clothes')

    #realizar transferencia a 'ropa' desde 'comida'
    food.transferir(300, clothes) 

    #mostrar libro mayor de 'ropa'
    print(clothes.registro)

    #consultar última transacción de 'comida' en el libro mayor
    print(food.registro[-1])