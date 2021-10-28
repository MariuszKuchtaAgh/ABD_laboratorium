import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category_id:int)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego id kategorii.
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category_id (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(category_id, int):
        request = f"""select f.title, l.name as languge, cat.name as category
                    from film f
                    join language l on l.language_id = f.language_id
                    join film_category fc on fc.film_id = f.film_id
                    join category cat on cat.category_id = fc.category_id
                    where cat.category_id = {category_id}
                    order by f.title, languge"""
    else:
        return None

    return pd.read_sql_query(request, con=connection)
    
def number_films_in_category(category_id:int)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o ilość filmów w zadanej kategori przez id kategorii.
    Przykład wynikowej tabeli:
    |   |category   |count|
    |0	|Action 	|64	  | 
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    category_id (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(category_id, int):
        request = f"""select distinct cat.name as category, count(cat.name) 
                    from film f  
                    join film_category fc on fc.film_id = f.film_id
                    join category cat on cat.category_id = fc.category_id  
                    where cat.category_id = {category_id}
                    group by cat.name"""
    else:
        return None

    return pd.read_sql_query(request, con=connection)

def number_film_by_length(min_length: Union[int,float] = 0, max_length: Union[int,float] = 1e6 ) :
    ''' Funkcja zwracająca wynik zapytania do bazy o ilość filmów o dla poszczegulnych długości pomiędzy wartościami min_length a max_length.
    Przykład wynikowej tabeli:
    |   |length     |count|
    |0	|46 	    |64	  | 
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    min_length (int,float): wartość minimalnej długości filmu
    max_length (int,float): wartość maksymalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if (isinstance(min_length, int) or isinstance(min_length, float)) and (isinstance(max_length, int) or isinstance(max_length, float)):
        if min_length < max_length:
            request = f"""select distinct f.length, count(*) 
                        from film f 
                        where f.length <= {max_length} and f.length >= {min_length}
                        group by f.length
                        order by f.length asc"""
        else:
            return None
    else:
        return None

    return pd.read_sql_query(request, con=connection)

def client_from_city(city:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o listę klientów z zadanego miasta przez wartość city.
    Przykład wynikowej tabeli:
    |   |city	    |first_name	|last_name
    |0	|Athenai	|Linda	    |Williams
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    city (str): nazwa miaste dla którego mamy sporządzić listę klientów
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(city, str):
        request = f"""select ct.city as city, cs.first_name as first_name, cs.last_name as last_name
                    from customer cs 
                    join address ad on ad.address_id = cs.address_id 
                    join city ct on ct.city_id = ad.city_id 
                    where ct.city = \'{city}\'
                    order by first_name"""
    else:
        return None

    return pd.read_sql_query(request, con=connection)

def avg_amount_by_length(length:Union[int,float])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o średnią wartość wypożyczenia filmów dla zadanej długości length.
    Przykład wynikowej tabeli:
    |   |length |avg
    |0	|48	    |4.295389
    
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    length (int,float): długość filmu dla którego mamy pożyczyć średnią wartość wypożyczonych filmów
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(length, int) or isinstance(length, float):
        request = f"""select f.length as length, AVG(p.amount) as avg
                    from film f
                    join inventory i on i.film_id = f.film_id
                    join rental r on r.inventory_id = i.inventory_id
                    join payment p on p.rental_id = r.rental_id
                    where f.length = {length}
                    group by f.length"""
    else:
        return None

    return pd.read_sql_query(request, con=connection)

def client_by_sum_length(sum_min:Union[int,float])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o sumaryczny czas wypożyczonych filmów przez klientów powyżej zadanej wartości .
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |sum
    |0  |Brian	    |Wyman  	|1265
    
    Tabela wynikowa powinna być posortowane według sumy, nazwiska i imienia klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    sum_min (int,float): minimalna wartość sumy długości wypożyczonych filmów którą musi spełniać klient
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(sum_min, int) or isinstance(sum_min, float):
        request = f"""select cs.first_name as first_name, cs.last_name as last_name, SUM(f.length) as sum
                    from film f
                    join inventory i on i.film_id = f.film_id
                    join rental r on r.inventory_id = i.inventory_id
                    join customer cs on cs.customer_id = r.customer_id
                    group by cs.first_name, cs.last_name
                    having SUM(f.length) > {sum_min}  
                    order by sum, last_name, first_name"""
    else:
        return None

    return pd.read_sql_query(request, con=connection)

def category_statistic_length(name:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o statystykę długości filmów w kategorii o zadanej nazwie.
    Przykład wynikowej tabeli:
    |   |category   |avg    |sum    |min    |max
    |0	|Action 	|111.60 |7143   |47 	|185
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    name (str): Nazwa kategorii dla której ma zostać wypisana statystyka
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(name, str):
        request = f"""select cat.name as category, AVG(f.length) as avg, SUM(f.length) as sum, MIN(f.length) as min, MAX(f.length) as max
                    from category cat
                    join film_category fc on fc.category_id = cat.category_id
                    join film f on f.film_id = fc.film_id
                    where cat.name = \'{name}\'
                    group by cat.name """
    else:
        return None

    return pd.read_sql_query(request, con=connection)