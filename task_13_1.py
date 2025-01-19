import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(10 / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')


async def start_tournament(mans):
    smans = []
    for man, power in mans.items():
        smans.append(asyncio.create_task(start_strongman(man, power)))
    for x in smans:
        await x


strongmans = {'Pasha': 3, 'Denis': 4, 'Apollon': 5}

asyncio.run(start_tournament(strongmans))
