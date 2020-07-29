from api.animethemes import AnimeThemes
from api.openingsmoe import OpeningsMoe

from utils.utils import Utils

import pandas as pd
import numpy as np

import sys, traceback

class Facade():
    def __init__(self):
        try:
            self.song_set = AnimeThemes().get_openings_list()
        except:
            self.song_set = OpeningsMoe().get_openings_list()

        self.__init_modules()

        self.title_list = self.utils.get_unique_names(self.song_set, 'Anime_Title')

    def __init_modules(self) -> None:
        self.utils = Utils() # db processing

    def __song_type(self, song_type: int) -> str:
        if song_type == 1:
            return 'OP'
        elif song_type == 2:
            return 'ED'
        elif song_type == 3:
            return 'Insert'
        else:
            return ""

    def __song_type_handle(self, df: pd.DataFrame, song_type: int) -> pd.DataFrame:
        contains = self.__song_type(song_type)

        return df[df['Song_Type'].str.contains(contains)]

    def __get_animes_with_exact_titles(self, df: pd.DataFrame, titles: list) -> pd.DataFrame:
        resp = df[df['Anime_Title'].isin(titles)]

        return resp

    def __get_anime_with_exact_title(self, df: pd.DataFrame, title: str) -> dict:
        resp: pd.DataFrame = df[df['Anime_Title'] == title]

        if resp.empty:
            resp: pd.DataFrame = df[df['Anime_Title'].str.lower() == title]

        return resp.to_dict('r')

    def __find_anime_by_query(self, title: str) -> list:    
        response = self.utils.find_simillar(self.title_list, title)

        return response

    def get_songs_by_title(self, title: str, exact: bool = False) -> list:
        response_list = []

        if exact:
            response_list += self.__get_anime_with_exact_title(self.song_set, title.lower())

        else:
            titles_list = self.__find_anime_by_query(title)
            for title_tmp in titles_list:
                response_list += self.__get_anime_with_exact_title(self.song_set, title_tmp.lower())
            
        return {
            'count': len(response_list),
            'items': response_list
        }

    def get_random_webms(self, count: int, song_type: int = 4, df: pd.DataFrame = None) -> dict:
        try:
            if type(df) != pd.DataFrame:
                df = self.song_set
                
            if song_type in [1, 2, 3]:
                df = self.__song_type_handle(df, song_type)

            response = df.sample(n=count, replace=True, random_state=np.random.randint(1, 10000000))

            return {
                'count': count,
                'items': response.to_dict('r')
            }

        except Exception:
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)

            return {
                'count': 0,
                'items': []
            }

    def get_random_webms_by_anime_title(self, count: int, title: str, song_type: int = 4) -> dict:
        try:
            titles_list = self.__find_anime_by_query(title)

            df = self.__get_animes_with_exact_titles(self.song_set, titles_list)
            
            return self.get_random_webms(count=count,
                                        song_type=song_type,
                                        df=df)

        except Exception:
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)

            return {
                'count': 0,
                'items': []
            }

    def get_list_of_songs_sorted(self, count: int = None, song_type: int = 4) -> dict:
        try:
            df = self.song_set.sort_values(by='Song_Title')

            resp = self.__song_type_handle(df=df, 
                                song_type=song_type)

            resp = resp.to_dict('r')

            count_by_len = len(resp.index)
            if count:
                if count_by_len > count:
                    resp = resp[:count]
                else:
                    count = count_by_len
            else:
                count = count_by_len

            return {
                'count': count,
                'items': resp
            }

        except Exception:
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)

            return {
                'count': 0,
                'items': []
            }

    def get_list_of_animes(self, count: int = None) -> dict:
        try:
            resp = list(self.song_set['Anime_Title'].unique())

            count_by_len = len(resp)
            if count:
                if count_by_len > count:
                    resp = resp[:count]
                else:
                    count = count_by_len
            else:
                count = count_by_len
            
            return {
                'count': count,
                'items': resp
            }

        except Exception:
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)

            return {
                'count': 0,
                'items': []
            }