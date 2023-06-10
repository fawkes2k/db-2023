from asyncio import run
import asyncpg
from dotenv import load_dotenv
from os import getenv
from model import *

load_dotenv()
URL = getenv('DATABASE_URL')
SCHEMA = getenv('SCHEMA')


class DbService:

    async def initialize(self):
        self.pool = await asyncpg.create_pool(URL, timeout=30, command_timeout=5, server_settings={'search_path': SCHEMA})

    async def get_videos(self, offset=0, limit=500) -> list[Video]:
        async with self.pool.acquire() as connection:
            rows = await connection.fetch('select * from video order by title offset $1 limit $2', offset, limit)
        return [Video(**dict(r)) for r in rows]

    async def set_like(self, video_id: UUID, user_id: UUID, like_level: bool):
        async with self.pool.acquire() as connection:
            await connection.fetch('insert into video_likes(video_id, channel_id, is_like)'
                                   'values ($1, $2, $3) returning *', video_id, user_id, like_level)

    async def post_comment(self, user_id: UUID, content: str, video_id: UUID, comment_parent_id: UUID | None):
        async with self.pool.acquire() as connection:
            await connection.fetch('insert into comment(author, content, video_id, parent_comment) values'
                                   '($1, $2, $3, $4) returning *', user_id, content, video_id, comment_parent_id)


async def main_():
    db = DbService()
    await db.initialize()
    videos = await db.get_videos()
    print(videos)
    video, user = UUID('771c8d3e-1c32-4a9b-9cb1-6c278b52580c'), UUID('8aa66945-77b2-4bb2-bd17-00da523c561e')
    await db.set_like(video, user, True)
    await db.post_comment(user, 'test', video, None)

if __name__ == '__main__':
    run(main_())
