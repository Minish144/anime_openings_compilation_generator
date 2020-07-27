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

    def __song_type_handle(self, df: pd.DataFrame, song_type: int) -> pd:
        contains = self.__song_type(song_type)
        return df[df['Song_Type'].str.contains(contains)]

    def get_random_webms(self, count: int, song_type: int = 3) -> dict:
        if song_type in [1, 2]:
            df = self.__song_type_handle(self.song_set, song_type)
        else:
            df = self.song_set
        response = df.sample(n=count, replace=False, random_state=np.random.randint(1, 100000000))
        
        return {
            'count': count,
            'items': response.to_dict('r')
        }

    def find_simillar(self, column: str, req: str):
        self.utils.find_simillar(self.song_set, "col", req)