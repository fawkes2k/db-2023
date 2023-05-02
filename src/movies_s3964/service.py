from src.movies.db_service import *
from objects import *

class Service(DbService):
    async def get_languages(self, offset=0, limit=500) -> list[Language]:
        async with self.pool.acquire() as connection:
            rows = await connection.fetch('select * from language order by name offset $1 limit $2', offset, limit)
        return [Language(**dict(r)) for r in rows]

    async def get_language(self, iso_639_1: str) -> Language | None:
        async with self.pool.acquire() as connection:
            row = await connection.fetchrow('select * from language where iso_639_1=$1', iso_639_1)
        return Language(**dict(row)) if row else None

    async def upsert_language(self, language: Language) -> Language:
        if language.iso_639_1 is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into language(name) VALUES ($1) returning *",
                                                language.name)
        elif await self.get_language(language.iso_639_1) is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into language(iso_639_1, name) VALUES ($1,$2) returning *",
                                                language.iso_639_1, language.name)
        else:
            # update
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("""update language set name=$2 where iso_639_1=$1 returning *""",
                                                language.iso_639_1, language.name)
        return Language(**dict(row))

    async def get_movies_languages(self, movie_id: int, iso_639_1: str) -> list[MovieLanguage]:
        async with self.pool.acquire() as connection:
            rows = await connection.fetch('select * from movie_language where movie_id=$1 and iso_639_1=$2', movie_id, iso_639_1)
        return [MovieLanguage(**dict(r)) for r in rows]

    async def get_movie_languages(self, movie_id: int) -> list[MovieLanguage] | None:
        async with self.pool.acquire() as connection:
            rows = await connection.fetchrow('select * from movie_language where movie_id=$1', movie_id)
        return [MovieLanguage(**dict(r)) for r in rows]

    async def get_language_movies(self, iso_639_1: str) -> list[MovieLanguage] | None:
        async with self.pool.acquire() as connection:
            rows = await connection.fetchrow('select * from movie_language where iso_639_1=$1', iso_639_1)
        return [MovieLanguage(**dict(r)) for r in rows]

    async def upsert_movie_language(self, movie_language: MovieLanguage) -> MovieLanguage:
        if len(await self.get_movies_languages(movie_language.movie_id, movie_language.iso_639_1)) == 0:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into movie_language(movie_id, iso_639_1) VALUES "
                                                "($1,$2) returning *",
                                                movie_language.movie_id, movie_language.iso_639_1)
            return MovieLanguage(**dict(row))

    async def get_pcompanies(self, offset=0, limit=500) -> list[PCompany]:
        async with self.pool.acquire() as connection:
            rows = await connection.fetch('select * from pcompany order by name offset $1 limit $2', offset, limit)
        return [PCompany(**dict(r)) for r in rows]

    async def get_pcompany(self, company_id: int) -> PCompany | None:
        async with self.pool.acquire() as connection:
            row = await connection.fetchrow('select * from pcompany where id=$1', company_id)
        return PCompany(**dict(row)) if row else None

    async def upsert_pcompany(self, company: PCompany) -> PCompany:
        if company.id is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into pcompany(name) VALUES ($1) returning *",
                                                company.name)
        elif await self.get_pcompany(company.id) is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into pcompany(id, name) VALUES ($1,$2) returning *",
                                                company.id, company.name)
        else:
            # update
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("""update pcompany set name=$2 where id=$1 returning *""",
                                                company.id, company.name)
        return PCompany(**dict(row))

    async def get_movie_company(self, movie_id: int, company_id: int) -> MovieCompany | None:
        async with self.pool.acquire() as connection:
            row = await connection.fetchrow('select * from movie_company where movie_id=$1 and company_id=$2', movie_id, company_id)
        return MovieCompany(**dict(row)) if row else None

    async def get_movie_companies(self, movie_id: int) -> list[MovieCompany] | None:
        async with self.pool.acquire() as connection:
            rows = await connection.fetchrow('select * from movie_company where movie_id=$1', movie_id)
        return [MovieCompany(**dict(r)) for r in rows]

    async def get_company_movies(self, company_id: int) -> list[MovieCompany] | None:
        async with self.pool.acquire() as connection:
            rows = await connection.fetchrow('select * from movie_company where company_id=$1', company_id)
        return [MovieCompany(**dict(r)) for r in rows]

    async def upsert_movie_company(self, movie_company: MovieCompany) -> MovieCompany:
        if await self.get_movie_company(movie_company.movie_id, movie_company.company_id) is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into movie_company(movie_id, company_id) VALUES "
                                                "($1,$2) returning *",
                                                movie_company.movie_id, movie_company.company_id)
            return MovieCompany(**dict(row))

    async def get_keywords(self, offset=0, limit=500) -> list[Keyword]:
        async with self.pool.acquire() as connection:
            rows = await connection.fetch('select * from keyword order by name offset $1 limit $2', offset, limit)
        return [Keyword(**dict(r)) for r in rows]

    async def get_keyword(self, keyword_id: int) -> Keyword | None:
        async with self.pool.acquire() as connection:
            row = await connection.fetchrow('select * from keyword where id=$1', keyword_id)
        return Keyword(**dict(row)) if row else None

    async def upsert_keyword(self, keyword: Keyword) -> Keyword:
        if keyword.id is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into keyword(name) VALUES ($1) returning *",
                                                keyword.name)
        elif await self.get_keyword(keyword.id) is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into keyword(id, name) VALUES ($1,$2) returning *",
                                                keyword.id, keyword.name)
        else:
            # update
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("""update keyword set name=$2 where id=$1 returning *""",
                                                keyword.id, keyword.name)
        return Keyword(**dict(row))

    async def get_movie_keyword(self, movie_id: int, keyword_id: int) -> MovieKeyword | None:
        async with self.pool.acquire() as connection:
            row = await connection.fetchrow('select * from movie_keyword where movie_id=$1 and keyword_id=$2', movie_id,
                                            keyword_id)
        return MovieKeyword(**dict(row)) if row else None

    async def get_movie_keywords(self, movie_id: int) -> list[MovieKeyword] | None:
        async with self.pool.acquire() as connection:
            rows = await connection.fetchrow('select * from movie_keyword where movie_id=$1', movie_id)
        return [MovieKeyword(**dict(r)) for r in rows]

    async def get_keyword_movies(self, keyword_id: int) -> list[MovieKeyword] | None:
        async with self.pool.acquire() as connection:
            rows = await connection.fetchrow('select * from movie_keyword where keyword_id=$1', keyword_id)
        return [MovieKeyword(**dict(r)) for r in rows]

    async def upsert_movie_keyword(self, movie_keyword: MovieKeyword) -> MovieKeyword:
        if await self.get_movie_keyword(movie_keyword.movie_id, movie_keyword.keyword_id) is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into movie_keyword(movie_id, keyword_id) VALUES "
                                                "($1,$2) returning *",
                                                movie_keyword.movie_id, movie_keyword.keyword_id)
            return MovieKeyword(**dict(row))