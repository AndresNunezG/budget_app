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
        description = f'Transfer to {transfer_to}'
        successful_transfer = self.withdraw(amount, description)
        if successful_transfer:
            description = f'Transfer from {self.name}'
            transfer_to.deposit(amount, )
            return True
        else:
            return False
            
if __name__ == '__main__':
    food = category('food')
    food.deposit(200, 'cheetos')
    food.deposit(150, 'sandwich')

    print(food.get_balance())
    print(food.check_funds(400))