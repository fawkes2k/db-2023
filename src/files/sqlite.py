from aiosqlite import connect
from asyncio import run
from model import File

class SQLite:
    async def initialize(self, file: str):
        self.connection = await connect(file)
        print('Connected!')

    async def get_files(self, limit=500) -> list[File]:
        rows = await self.connection.execute_fetchall('select * from files order by basename limit $1', [limit])
        return [File(*r) for r in rows]

    async def get_file(self, file_id: int) -> File | None:
        row = await self.connection.execute_fetchall('select * from files where fileid = $1', [file_id])
        return File(*row[0]) if len(row) > 0 else None


async def main_():
    sqlite = SQLite()
    await sqlite.initialize('database.sqlite')
    files = await sqlite.get_files()
    file = await sqlite.get_file(2023)
    print(files[111])
    print(file)

if __name__ == '__main__':
    run(main_())
