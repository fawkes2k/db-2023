from dataclasses import dataclass


@dataclass
class Language:
    iso_639_1: str
    name: str

@dataclass
class MovieLanguage:
    movie_id: int
    iso_639_1: str

@dataclass
class PCompany:
    id: int
    name: str

@dataclass
class MovieCompany:
    movie_id: int
    company_id: int

@dataclass
class Keyword:
    id: int
    name: str

@dataclass
class MovieKeyword:
    movie_id: int
    keyword_id: int
