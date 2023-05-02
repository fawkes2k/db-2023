from json import loads
import pandas as pd
from objects import *

df = pd.read_csv('data/tmdb_5000_movies.csv')


def get_languages() -> list[Language]:
    vals = []
    for x in df['spoken_languages']:
        for y in loads(x):
            obj = Language(**y)
            if obj not in vals: vals.append(obj)
    return vals


def get_movie_languages() -> list[MovieLanguage]:
    vals = []
    for index, language in enumerate(df['spoken_languages']):
        movie_id = df['id'][index]
        for y in loads(language):
            obj = MovieLanguage(movie_id, y['iso_639_1'])
            if obj not in vals: vals.append(obj)
    return vals


def get_pcompany() -> list[PCompany]:
    vals = []
    for x in df['production_companies']:
        for y in loads(x):
            obj = PCompany(**y)
            if obj not in vals: vals.append(obj)
    return vals


def get_movie_company() -> list[MovieCompany]:
    vals = []
    for index, language in enumerate(df['production_companies']):
        movie_id = df['id'][index]
        for y in loads(language):
            obj = MovieCompany(movie_id, y['id'])
            if obj not in vals: vals.append(obj)
    return vals


def get_keywords() -> list[Keyword]:
    vals = []
    for x in df['keywords']:
        for y in loads(x):
            obj = Keyword(**y)
            if obj not in vals: vals.append(obj)
    return vals


def get_movie_keywords() -> list[MovieKeyword]:
    vals = []
    for index, language in enumerate(df['keywords']):
        movie_id = df['id'][index]
        for y in loads(language):
            obj = MovieKeyword(movie_id, y['id'])
            if obj not in vals: vals.append(obj)
    return vals
