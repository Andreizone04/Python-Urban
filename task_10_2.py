import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        day_battles = 0
        print(f'{self.name}, на нас напали!')
        enemies = 100
        while enemies > 0:
            day_battles += 1
            enemies -= self.power
            time.sleep(1)
            print(f'{self.name} сражается {day_battles}..., осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {day_battles} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
