from threading import Thread
import time
import random
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # Симулируем ожидание от 3 до 10 секунд
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            assigned = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    assigned = True
                    break
            if not assigned:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    guest = table.guest
                    if not guest.is_alive():
                        print(f'{guest.name} покушал(-а) и ушёл(-ла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                        # Если очередь не пуста, посаживаем следующего гостя за свободный стол
                        if not self.queue.empty():
                            next_guest = self.queue.get()
                            table.guest = next_guest
                            next_guest.start()
                            print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
                'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
                ]
# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()