from queue import Queue
from threading import Thread
from time import sleep
from random import random


class Table():
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self, daemon=False)
        self.name = name

    def run(self):
        sleep(3 + random() * 7)


class Cafe():
    def __init__(self, *args):
        self.tables = []
        for i in args:
            if type(i) == Table: self.tables.append(i)
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for g in guests:
            sit_avail = False
            for i in range(len(self.tables)):
                if self.tables[i].guest is None:
                    self.tables[i].guest = g
                    self.tables[i].guest.start()
                    sit_avail = True
                    print(f'{g.name} сел за стол номер {self.tables[i].number}')
                    break
            if not sit_avail:
                self.queue.put(g)
                print(f'{g.name} в очереди')

    def discuss_guests(self):
        is_customers = True
        while is_customers:
            is_customers = False
            for i in range(len(self.tables)):
                if not self.tables[i].guest is None:
                    is_customers = True
                    if self.tables[i].guest.is_alive() is False:
                        print(f'{ self.tables[i].guest.name} покушал и ушел(а)')
                        print(f'Стол номер {self.tables[i].number} свободен')
                        if not self.queue.empty():
                            self.tables[i].guest = self.queue.get()
                            self.tables[i].guest.start()
                            print(
                                f'{self.tables[i].guest.name} вышел из очереди и сел за стол номер {self.tables[i].number}')
                        else:
                            self.tables[i].guest = None

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
