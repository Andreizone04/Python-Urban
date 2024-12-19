import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(1, 101):
            a = random.randint(50, 500)
            self.balance += a
            print(f'Пополнение: {a}. Баланс: {self.balance} | номер операции = {i}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
        time.sleep(0.001)

    def take(self):
        for i in range(1, 101):
            a = random.randint(50, 500)
            print(f'Запрос на {a}')
            if a <= self.balance:
                self.balance -= a
                print(f'Снятие: {a}. Баланс: {self.balance} | номер операции = {i}')
            else:
                print(f'Запрос отклонён, недостаточно средств | номер операции = {i}')
                self.lock.acquire()
        time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
