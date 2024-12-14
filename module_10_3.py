import threading
from random import random
from time import sleep


class Bank():
    def __init__(self):
        self.balance=0
        self.lock=threading.Lock()
        self.stop=False

    def deposit(self):
        tact_count=100
        amount=0
        while tact_count>0:
            if self.lock.locked():
                if self.balance>=500:self.lock.release()
            amount=round(50+random()*450,2)
            print(f'Пополнение на {amount} ')
            self.balance = round(amount+self.balance,2)
            tact_count -= 1
            sleep(random()*0.001)
        if self.lock.locked():self.lock.release()
        self.stop=True

    def take(self):
        tact_count = 100
        amount = 0
        while tact_count>0:
            amount = round(50+random() * 450,2)
            print(f'Запрос на {amount} ')
            if amount<=self.balance:
                self.balance=round(self.balance-amount,2)
                print(f'Снятие {amount}. Текущий баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                if not self.stop:self.lock.acquire()
            tact_count-=1
            sleep(random()*0.001)

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
if bk.lock.locked():bk.lock.release()
print(f'Итоговый баланс: {bk.balance}')

x=random()