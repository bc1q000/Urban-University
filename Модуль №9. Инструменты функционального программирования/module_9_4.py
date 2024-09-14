from random import choice

#  Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

f1 = list(map(lambda x, y: x == y, first, second))
print(f1)


#  Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a+', encoding='utf-8') as file:
            # Приводим все элементы в data_set к строковому типу и записываем
            file.writelines([str(item) + '\n' for item in data_set])
            # Перемещаем указатель в начало для чтения содержимого
            file.seek(0)
            result = file.read()
            return result

    return write_everything('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

print(get_advanced_writer('example.txt'))





#  Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *args, **kwargs):
        print('Сработал магический метод __call__')
        chosen_word = choice(self.words)
        return chosen_word

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())