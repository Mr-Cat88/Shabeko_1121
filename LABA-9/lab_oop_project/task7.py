# задание7. мой класс

class Product:

    def __init__(self, product_id, name, price, quantity=0):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def apply_discount(self, percent):
        if 0 <= percent <= 100:
            discount = self.price * percent / 100
            self.price -= discount
            print(f"скидка {percent}% применена. новая цена: {self.price:.2f} руб.")
        else:
            print("неверный процент скидки")

    def display_info(self):
        print(f"товар ID: {self.id}")
        print(f"название: {self.name}")
        print(f"цена: {self.price:.2f} руб.")
        print(f"количество на складе: {self.quantity}")


# создание объекта product
product = Product(1, "ноутбук aser", 45000, 10)

# вывод инфо о товаре
print("информация о товаре:")
product.display_info()

# применение скидки
print("\nприменение скидки:")
product.apply_discount(10)
product.display_info()

# отчет хд
print("объяснение выбора класса:")
print("""
почему выбран класс product:
1. товары это основная сущность в информационных системах магазинов
2. атрибуты (id, name, price, quantity) необходимы для учёта товаров
3. метод apply_discount() частая бизнес-операция (скидка)
4. класс можно использовать для реальной системы (добавить категорию, описание и еще че нибудь) 
""")