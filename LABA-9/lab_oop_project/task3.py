# задание3. класс Account для банковской системы

class Account:
    def __init__(self, owner, balance=0):
        # конструктор с owner и balance
        self.owner = owner
        self.balance = balance
        print(f"создан счёт для {owner}. начальный баланс: {balance} руб.")

    def deposit(self, amount):
        # метод для пополнения счёта
        self.balance += amount
        print(f"счёт пополнен на {amount} руб.")


# создание счёта
account = Account("иван петров", 1000)

# пополнение счёта
account.deposit(500)

# вывод баланса
print(f"итоговый баланс: {account.balance} руб.")