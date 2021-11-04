import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str, dokładnie taki jak podana wartość
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''

    if isinstance(category, int):
        req = f"""
                select f.title as title, lang.name as languge, cat.name as category
                from film f 
                join language lang on lang.language_id = f.language_id
                join film_category fcat on fcat.film_id = f.film_id
                join category cat on cat.category_id = fcat.category_id
                where cat.category_id = {category}
                order by f.title, lang.name
        """
    elif isinstance(category, str):
        req = f"""
                select f.title as title, lang.name as languge, cat.name as category
                from film f 
                join language lang on lang.language_id = f.language_id
                join film_category fcat on fcat.film_id = f.film_id
                join category cat on cat.category_id = fcat.category_id
                where cat.name = '{category}'
                order by f.title, lang.name
        """
    else:
        return None

    return pd.read_sql_query(req, con=connection)
    
def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''

    if isinstance(category, int):
        req = f"""
                select f.title as title, lang.name as languge, cat.name as category
                from film f 
                join language lang on lang.language_id = f.language_id
                join film_category fcat on fcat.film_id = f.film_id
                join category cat on cat.category_id = fcat.category_id
                where cat.category_id = {category}
                order by f.title, lang.name
        """
    elif isinstance(category, str):
        req = f"""
                select f.title as title, lang.name as languge, cat.name as category
                from film f 
                join language lang on lang.language_id = f.language_id
                join film_category fcat on fcat.film_id = f.film_id
                join category cat on cat.category_id = fcat.category_id
                where cat.name ~~* '{category}'
                order by f.title, lang.name
        """
    else:
        return None

    return pd.read_sql_query(req, con=connection)
    
def film_cast(title:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |
    |0	|Greg       |Chaplin    | 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    title (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(title, str):
        req = f"""
                select act.first_name as first_name, act.last_name as last_name
                from film f 
                join film_actor fact on fact.film_id = f.film_id
                join actor act on act.actor_id = fact.actor_id
                where f.title = '{title}'
                order by act.last_name, act.first_name
        """
    else:
        return None

    return pd.read_sql_query(req, con=connection)
    

def film_title_case_insensitive(words:list) :
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
    Przykład wynikowej tabeli:
    |   |title              |
    |0	|Crystal Breaking 	| 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    words(list): wartość minimalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(words, list) and all(isinstance(word, str) for word in words):
        reg = "(^.*" + ".*$)|(^.*".join(words) + ".*$)"
        # reg = "(.*\b" + "\b.*)|(.*\b".join(words) + "\b.*)"
        # reg = "(\b" + "\b)|(\b".join(words) + "\b)"
        req = f"""
                select f.title as title
                from film f 
                where f.title ~* '{reg}'
                order by f.title
        """
    else:
        return None

    return pd.read_sql_query(req, con=connection)