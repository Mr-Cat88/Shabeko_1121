# задание6. полиморфизм

class WebPage:
    def __init__(self, title):
        self.title = title

    def show(self):
        print(f"название страницы: {self.title}")


class SpecialPage(WebPage):
    def __init__(self, title, description):
        # вызов конструктора родительского класса
        super().__init__(title)
        # добав нового атрибута
        self.description = description

    def show(self):
        print(f"название страницы: {self.title}")
        print(f"описание: {self.description}")


# создание объектов
page1 = WebPage("главная страница")
page2 = SpecialPage("акции", "скидки на все товары")

# вызов метода show() для 2 объектов
print("веб-страница:")
page1.show()

print("\nспециальная страница:")
page2.show()