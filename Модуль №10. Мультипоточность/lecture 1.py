# Запрос на сайт
import requests
from datetime import datetime

# Поток
from threading import Thread

# Запрос на сайт
time_start = datetime.now()

THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
res = []
for i in range(10):
    response = requests.get(THE_URL)
    page_response = response.json()
    res.append(page_response)

time_end = datetime.now()
time_res = time_end - time_start

print(time_res)
print(res)



# Поток
res = []
time_start = datetime.now()
def func(url):
    response = requests.get(THE_URL)
    page_response = response.json()
    res.append(page_response)

thr_fr = Thread(target=func, args=(THE_URL, ))
thr_sc = Thread(target=func, args=(THE_URL, ))
thr_fhr = Thread(target=func, args=(THE_URL, ))
thr_f4 = Thread(target=func, args=(THE_URL, ))
thr_f5 = Thread(target=func, args=(THE_URL, ))
thr_f6 = Thread(target=func, args=(THE_URL, ))
thr_f7 = Thread(target=func, args=(THE_URL, ))
thr_f8 = Thread(target=func, args=(THE_URL, ))
thr_f9 = Thread(target=func, args=(THE_URL, ))
thr_f10 = Thread(target=func, args=(THE_URL, ))

thr_fr.start()
thr_sc.start()
thr_fhr.start()
thr_f4.start()
thr_f5.start()
thr_f6.start()
thr_f7.start()
thr_f8.start()
thr_f9.start()
thr_f10.start()

thr_fr.join()
thr_sc.join()
thr_fhr.join()
thr_f4.join()
thr_f5.join()
thr_f6.join()
thr_f7.join()
thr_f8.join()
thr_f9.join()
thr_f10.join()

time_end = datetime.now()
time_res = time_end - time_start

print(time_res)
print(res)