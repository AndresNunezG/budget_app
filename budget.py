class category():
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount':amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -1*amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for movements in self.ledger:
            balance += movements['amount']
        return balance

    def check_funds(self, amount):
        return False if amount > self.get_balance() else True
    
    def transfer(self, amount, transfer_to):
        description = f'Transfer to {transfer_to.name}'
        successful_transfer = self.withdraw(amount, description)
        if successful_transfer:
            description = f'Transfer from {self.name}'
            transfer_to.deposit(amount, description)
            return True
        else:
            return False

if __name__ == '__main__':
    
    #crear categoria de comida y agregar depositos y retiros
    food = category('food')
    food.deposit(200, 'deposit 1')
    food.deposit(350, 'deposit 2')
    food.withdraw(100, 'sandwich')

    #imprimir balance de la categoria comida
    print('Balance categoría food: ', end='')
    print(food.get_balance())

    #verificar si se cuenta con una cantidad de 400 disponible
    print('400 disponibles?: ', end='')
    print(food.check_funds(400))

    #crear categoría de ropa
    clothes = category('clothes')

    #realizar transferencia a 'ropa' desde 'comida'
    food.transfer(300, clothes) 

    #mostrar libro mayor de 'ropa'
    print(clothes.ledger)

    #consultar última transacción de 'comida' en el libro mayor
    print(food.ledger[-1])