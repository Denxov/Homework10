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
        self.queue.
