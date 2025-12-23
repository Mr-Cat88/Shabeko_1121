# задание1. простой класс без методов

class Car:
    wheels = 4
    seats = 5
    color = "красный"
    brand = "toyota"

my_car = Car()

# вывод
print("атрибуты автомобиля:")
print(f"количество колёс: {my_car.wheels}")
print(f"число пассажирских мест: {my_car.seats}")
print(f"цвет: {my_car.color}")
print(f"марка: {my_car.brand}")