import threading
from datetime import datetime
from time import sleep

def write_words(word_count, file_name):
    with open(file_name,'w',encoding='utf-8') as file:
        for i in range(word_count):
            file.write('Какое то слово # '+str(i+1)+'\n')
            sleep(0.1)
    print('Завершилась запись в файл ' + file_name)

args=[10,30,200,100]
thread=[]

time_start=datetime.now()
for i in range(len(args)):
    write_words(args[i],f'Example{i+1}')
time_end=datetime.now()
print(f'Время работы  : {time_end-time_start}')

time_start=datetime.now()
for i in range(len(args)):
    thread.append(threading.Thread(target=write_words,args=(args[i],f'Example{i+5}')))
    thread[i].start()

for i in range(len(args)):thread[i].join()

time_end=datetime.now()
print(f'Время работы  : {time_end-time_start}')