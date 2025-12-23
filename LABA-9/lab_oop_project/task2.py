# задание2. класс Car с конструктором

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        # метод для вывода
        print(f"марка: {self.brand}")
        print(f"модель: {self.model}")
        print(f"год выпуска: {self.year}")


# создание объектов с разными значениями
car1 = Car("toyota", "camry", 2022)
car2 = Car("tesla", "model 3", 2023)

# вывод
print("автомобиль 1:")
car1.display_info()

print("\nавтомобиль 2:")
car2.display_info()