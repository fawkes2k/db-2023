import asyncio
from asyncio import run, sleep, create_task
from tools import *
from service import *

async def main():
    db = Service()
    await db.initialize()  # tu łączymy się z bazą danych

    movie_languages = get_movie_languages()
    print(len(movie_languages))
    tasks = []

    for i, movie_language in enumerate(movie_languages):
        tasks.append(create_task(db.upsert_movie_language(movie_language)))
        if i % 100 == 0:
            print(f'import in {i / len(movie_languages) * 100:.1f}% done')
            await asyncio.gather(*tasks)
            tasks = []

    await asyncio.gather(*tasks)
    await sleep(1)


if __name__ == '__main__':
    run(main())
