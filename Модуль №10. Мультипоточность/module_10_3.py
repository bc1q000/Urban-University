from threading import Thread, Lock
import random


class Bank:
    def __init__(self, balance, lock):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for deposit in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f'Пополнение: {amount}. Баланс: {self.balance}.')


    def take(self):
        for take in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                if self.balance >= amount:
                    self.balance -= amount
                    print(f'Запрос на {amount}\n'
                          f'Снятие: {amount}. Баланс: {self.balance}')
                else:
                    print(f'Запрос отклонён, недостаточно средств')


lock = Lock()
bk = Bank(balance=0, lock=lock)

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
