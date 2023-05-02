import asyncio
from asyncio import run, sleep, create_task
from tools import *
from service import *

async def main():
    db = Service()
    await db.initialize()  # tu łączymy się z bazą danych

    movie_keywords = get_movie_keywords()
    print(len(movie_keywords))
    tasks = []

    for i, movie_keyword in enumerate(movie_keywords):
        tasks.append(create_task(db.upsert_movie_keyword(movie_keyword)))
        if i % 100 == 0:
            print(f'import in {i / len(movie_keywords) * 100:.1f}% done')
            await asyncio.gather(*tasks)
            tasks = []

    await asyncio.gather(*tasks)
    await sleep(1)


if __name__ == '__main__':
    run(main())
