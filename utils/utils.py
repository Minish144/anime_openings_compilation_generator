import pandas as pd
import fuzzy_pandas as fpd

class Utils():
    def __init__(self):
        pass

    def find_simillar(self, df1: pd.DataFrame, column: str, req: str):
        df2 = pd.DataFrame(columns=['Request'])
        df2 = df2.append({'Request': req}, ignore_index=True)

        matches = fpd.fuzzy_merge(df1, df2,
                          left_on=['Anime_Title'],
                          right_on=['Request'],
                          ignore_case=True,
                          keep='match')

        print(matches['Anime_Title'])
    
    def get_unique_names(self, df: pd.DataFrame, column: str) -> list:
        return df[column].unique()