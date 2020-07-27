from api.animethemes import AnimeThemes
from api.openingsmoe import OpeningsMoe

from utils.utils import Utils

import pandas as pd
import numpy as np

class Facade():
    def __init__(self):
        try:
            self.song_set = AnimeThemes().get_openings_list()
        except:
            self.song_set = OpeningsMoe().get_openings_list()

        self.__init_modules()

        self.title_list = self.utils.get_unique_names(self.song_set, 'Anime_Title')

    def __init_modules(self):
        self.utils = Utils() # db processing

    def __song_type(self, song_type: int) -> str:
        if song_type == 1:
            return 'OP'
        elif song_type == 2:
            return 'ED'
        else:
            return 'OP'

    def __song_type_handle(self, df: pd.DataFrame, song_type: int) -> pd.DataFrame:
        contains = self.__song_type(song_type)
        
        return df[df['Song_Type'].str.contains(contains)]

    def __get_df_with_exact_titles(self, df: pd.DataFrame, titles: list) -> pd.DataFrame:
        print('titles list: ', titles)
        return df[df['Anime_Title'].str.lower().isin(titles)]

    def __find_anime_by_query(self, title: str) -> list:
        response = self.utils.find_simillar(self.title_list, title)
        print(response)

        return response

    def get_random_webms(self, count: int, song_type: int = 3, df: pd.DataFrame = None) -> dict:
        try:
            if type(df) != pd.DataFrame:
                df = self.song_set
                
            if song_type in [1, 2]:
                df = self.__song_type_handle(df, song_type)
            response = df.sample(n=count, replace=True, random_state=np.random.randint(1, 10000000))

            return {
                'count': count,
                'items': response.to_dict('r')
            }
        except Exception as e:
            print(e)

            return {
                'count': 0,
                'items': []
            }

    def get_random_webms_by_anime_title(self, count: int, title: str, song_type: int = 3) -> dict:
        titles_list = self.__find_anime_by_query(title)
        df = self.__get_df_with_exact_titles(self.song_set, titles_list)
        print(df)
        
        return self.get_random_webms(count=count,
                                    song_type=song_type,
                                    df=df)