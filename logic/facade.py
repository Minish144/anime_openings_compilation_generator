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
        elif song_type == 4:
            return 'Insert'
        else:
            return 'OP'

    def __song_type_handle(self, df: pd.DataFrame, song_type: int) -> pd.DataFrame:
        contains = self.__song_type(song_type)
        
        return df[df['Song_Type'].str.contains(contains)]

    def __get_animes_with_exact_titles(self, df: pd.DataFrame, titles: list) -> pd.DataFrame:
        resp = df[df['Anime_Title'].isin(titles)]

        return resp

    def __get_anime_with_exact_title(self, df: pd.DataFrame, title: str) -> dict:
        resp = df[df['Anime_Title'] == title]

        return resp.to_dict('r')

    def __find_anime_by_query(self, title: str) -> list:    
        response = self.utils.find_simillar(self.title_list, title)

        return response

    def get_songs_by_title(self, title: str) -> list:
        response_list = []
        titles_list = self.__find_anime_by_query(title)

        for title in titles_list:
            response_list += self.__get_anime_with_exact_title(self.song_set, title)
        
        return {
            'count': len(response_list),
            'items': response_list
        }

    def get_random_webms(self, count: int, song_type: int = 3, df: pd.DataFrame = None) -> dict:
        try:
            if type(df) != pd.DataFrame:
                df = self.song_set
                
            if song_type in [1, 2, 4]:
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

    def get_random_webms_by_anime_title(self, count: int, title: str, song_type: int = 3) -> dict:
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