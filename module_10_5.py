import multiprocessing
def read_info(name):
    all_data=[]
    with open(name,'r',encoding='utf-8') as file:
        all_data.append(file.readline())

if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    for i in filenames:
        read_info(i)

    process=[]
    for i in range(len(filenames)):
        process.append(multiprocessing.Process(target=read_info,args=filenames[i]))
        process[i].start()

