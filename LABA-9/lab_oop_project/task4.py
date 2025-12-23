# задание4. класс BankAccount с инкапсуляцией

class BankAccount:
    def __init__(self, owner, balance=0):
        # приватные атрибуты
        self.__owner = owner
        self.__balance = balance

    def get_balance(self):
        # метод для получения баланса (геттер)
        return self.__balance

    def set_balance(self, amount):
        # метод для изменения баланса (сеттер)
        if amount >= 0:
            self.__balance = amount
            print(f"баланс успешно изменён")
        else:
            print("баланс не может быть отрицательным")


# создание объекта BankAccount
account = BankAccount("мария иванова", 1000)

# вывод через геттер
print(f"начальный баланс: {account.get_balance()} руб.")

# изменение баланса на положительное значение
account.set_balance(1500)
print(f"баланс после изменения: {account.get_balance()} руб.")

# изменение баланса на отрицательное значение
account.set_balance(-500)
print(f"баланс после отрицательного изменения: {account.get_balance()} руб.")