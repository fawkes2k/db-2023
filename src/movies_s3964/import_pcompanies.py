import asyncio
from asyncio import run, sleep, create_task
from tools import *
from service import *

async def main():
    db = Service()
    await db.initialize()  # tu łączymy się z bazą danych

    pcompanies = get_pcompany()
    print(len(pcompanies))
    tasks = []

    for i, pcompany in enumerate(pcompanies):
        tasks.append(create_task(db.upsert_pcompany(pcompany)))
        if i % 100 == 0:
            print(f'import in {i / len(pcompanies) * 100:.1f}% done')
            await asyncio.gather(*tasks)
            tasks = []

    await asyncio.gather(*tasks)
    await sleep(1)


if __name__ == '__main__':
    run(main())
