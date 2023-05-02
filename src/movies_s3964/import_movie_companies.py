import asyncio
from asyncio import run, sleep, create_task
from tools import *
from service import *


async def main():
    db = Service()
    await db.initialize()  # tu łączymy się z bazą danych

    movie_companies = get_movie_company()
    print(len(movie_companies))
    tasks = []

    for i, movie_company in enumerate(movie_companies):
        tasks.append(create_task(db.upsert_movie_company(movie_company)))
        if i % 100 == 0:
            print(f'import in {i / len(movie_companies) * 100:.1f}% done')
            await asyncio.gather(*tasks)
            tasks = []

    await asyncio.gather(*tasks)
    await sleep(1)


if __name__ == '__main__':
    run(main())
