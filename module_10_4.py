from queue import Queue


class Table():
    def __init__(self,number,guest=None):
        self.number=number

class Guest(Thread):
    def __init__(self,name):
        self.name=name

    def run(self):
        sleep(3+random()*7)

class cafe():
    def __init__(self,*args):
        self.tables=[]
        for i in range(len(args)):
            self.tables.append()=args[i]
        self.queue=Queue(maxsize=len(args))

    def guest_arrival(self,*guests:Guest):
        for g in guests:
            sit_avail=False
            for i in range(len(self.tables)):
                if self.tables[i]==None:
                    self.tables[i]=g
                    self.tables[i].start()
                    self.tables[i].number=i+1
                    sit_avail=True
            if not sit_avail:self.queue.put(g)

    def discuss_quests(self):
        for i in range(len(self.tables)):
            if self.tables[i]!= None and self.tables[i].guest.is_alive():
                print(f'{self.tables[i].name} покушал и ушел Стол номер {self.tables[i].number} свободен')

