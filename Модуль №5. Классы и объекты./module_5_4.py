class House():
    houses_history = []  # Атрибут класса для хранения истории созданных зданий

    def __new__(cls, name, *args, **kwargs):  # Используется для переопределения, чтобы добавить историю создания
        instance = object.__new__(cls)  # Класс не наследуется от другого класса, а напрямую из объекта, поэтому не используем 'super()'
        cls.houses_history.append(name)  # Добавление в историю
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.__dict__['name']} снесён, но останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)