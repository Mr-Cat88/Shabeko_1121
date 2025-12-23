# задание5. наследование

class Person:
    def __init__(self, name, age):
        # Конструктор класса Person
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        # вызов конструктора родительского класса
        super().__init__(name, age)
        # добав нового атрибута
        self.student_id = student_id

# создание объекта студент
student = Student("алексей сидоров", 20, "STU12345")

# Вывод атр
print(f"имя: {student.name}")
print(f"возраст: {student.age}")
print(f"студенческий билет: {student.student_id}")