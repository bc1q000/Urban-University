from time import sleep
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w+', encoding='utf-8') as file:
        for num in range(1, word_count + 1):
            file.write('Какое-то слово №' + str(num) + '\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file.name}')


time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')



time_start = datetime.now()
def func(word_count, file_name):
    with open(file_name, 'w+', encoding='utf-8') as file:
        for num in range(1, word_count + 1):
            file.write('Какое-то слово №' + str(num) + '\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file.name}')

thr_fr = Thread(target = func, args = (10, 'example5.txt'))
thr_sc = Thread(target = func, args = (30, 'example6.txt'))
thr_fhr = Thread(target = func, args = (200, 'example7.txt'))
thr_f4 = Thread(target = func, args = (100, 'example8.txt'))

thr_fr.start()
thr_sc.start()
thr_fhr.start()
thr_f4.start()

thr_fr.join()
thr_sc.join()
thr_fhr.join()
thr_f4.join()

time_end = datetime.now()
time_res = time_end - time_start

print(time_res)