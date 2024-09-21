from threading import Thread
import requests


class Getter(Thread):
    res = []
    f = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'

    def run(self):
        response = requests.get(self.f)
        Getter.res.append(response.json())


threads = []
for i in range(10):
    thread = Getter()
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(Getter.res)
