import asyncio
from asyncio import run, sleep, create_task
from tools import *
from service import *

async def main():
    db = Service()
    await db.initialize()  # tu łączymy się z bazą danych

    languages = get_languages()
    print(len(languages))
    tasks = []

    for i, language in enumerate(languages):
        tasks.append(create_task(db.upsert_language(language)))
        if i % 100 == 0:
            print(f'import in {i / len(languages) * 100:.1f}% done')
            await asyncio.gather(*tasks)
            tasks = []

    await asyncio.gather(*tasks)
    await sleep(1)


if __name__ == '__main__':
    run(main())
