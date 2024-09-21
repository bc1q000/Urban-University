from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        days = 0
        enemies = 100
        print(f'{self.name}, на нас напали!')

        for enemies_last in range(enemies, 0, -(self.power)):
            sleep(1.0)
            days += 1
            print(f'{self.name} сражался {days} дней(дня), осталось {enemies_last - self.power} врагов')

            if enemies_last == 0:
                print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
first_knight.start()

second_knight = Knight("Sir Galahad", 20)
second_knight.start()


first_knight.join()
second_knight.join()


