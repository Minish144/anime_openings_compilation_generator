from api.animethemes import AnimeThemes
from api.openingsmoe import OpeningsMoe

import pandas as pd

class Facade():
    def __init__(self):
        self.themes = AnimeThemes().get_openings_list()
        self.moe = OpeningsMoe().get_openings_list()

    def __op_type(self, op_type: int) -> str:
        if op_type == 1:
            return 'OP'
        elif op_type == 2:
            return 'ED'
        else:
            return 'OP'

    def __op_type_handle(self, df: pd.DataFrame, op_type: int) -> pd:
        contains = self.__op_type(op_type)
        return df[~df.C.str.contains(contains)]

    def get_random_webms(self, count: int, op_type: int = 3):
        if op_type in [1, 2]:
            df = self.__op_type_handle(self.themes, op_type)
        else:
            df = self.themes
        response = df.sample(n=count, replace=False, random_state=1)
        return response