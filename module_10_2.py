from random import random
from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        Thread.__init__(self)
        self.name = name
        self.power = power
        self.delay = random()*0.2
        print(f'{name} на нас напали!')

    def run(self):
        enemy_count = 100
        day_count = 0
        while enemy_count > 0:
            sleep(1+self.delay)
            enemy_count -= self.power
            day_count += 1
            print(f'{self.name} сражается {day_count} дней, осталось {enemy_count} войнов')
        print(f'{self.name} одержал победу спустя {day_count} дней')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились')
