import multiprocessing
from datetime import datetime
from time import sleep


def read_info(name: str):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        all_data.append(file.read())


if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    started = datetime.now()

    for i in filenames:
        read_info(i)

    print(f'        Линия: {datetime.now() - started}')

    started = datetime.now()
    process = []
    for i in range(len(filenames)):
        process.append(multiprocessing.Process(target=read_info, args=(filenames[i],)))
        process[i].start()

    print(f'Мультипроцесс: {datetime.now() - started}')
