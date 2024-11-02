import asyncio
import time


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for ball_number in range(5):
        await asyncio.sleep(10/power)
        print(f'Силач {name} поднял {ball_number}')
    print(f'Силач {name} закончил соревнования')

async def start_turnament():
    print('Соревнования по поднятию мяча начались')
    await asyncio.sleep(1)
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3


start = time.time()
asyncio.run(start_turnament())
stop = time.time()

print(f'Турнир завершился за {round(stop-start, 2)} сек.')

# Без ассинхронности: Турнир завершился за 40.18 сек.
# С ассинхронностью: Турнир завершился за 17.74 сек.