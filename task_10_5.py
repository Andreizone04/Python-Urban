import time
from multiprocessing import Pool

all_data = []


def read_info(name):
    global all_data
    with open(name, 'r') as file:
        k = True
        while k == True:
            t = file.readline()
            if t != '':
                all_data.append(t)
            else:
                k = False


filenames = [f'./file {number}.txt' for number in range(1, 5)]
"""
start1 = time.time()

for file_name in read_files:
    read_info(filenames)

print(time.time() - start1, ' (линейный) ')
"""

all_data.clear()
process = []
start2 = time.time()

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        process = pool.map(read_info, filenames)

print(time.time() - start2, ' (многопроцессный) ')
