import threading
import time


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


files_parameters = [10, 30, 200, 100, ]
time_start = time.time()
file_number = 1
for i in files_parameters:
    wite_words(i, f'example{file_number}.txt')
    file_number += 1
time_1 = time.time() - time_start
print(f'Работа потоков {time_1}')
streams = []
time_start = time.time()
t = 0
for i in files_parameters:
    streams.append(threading.Thread(target=wite_words, args=(i, f'example{file_number}.txt')))
    streams[t].start()
    t += 1
    file_number += 1
for a in streams:
    a.join()

time_2 = time.time() - time_start
print(f'Работа потоков {time_2}')
