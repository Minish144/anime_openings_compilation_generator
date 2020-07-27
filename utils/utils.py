import pandas as pd
from fuzzywuzzy import fuzz
import string

class Utils():
    def __init__(self):
        pass

    def find_simillar(self, lst: list, req: str):
        response_list = []

        for elem in lst:
            if req in elem:
                response_list.append(elem)
            elif fuzz.ratio(elem, req) > 60:
                response_list.append(elem)

    def get_unique_names(self, df: pd.DataFrame, column: str) -> list:
        return df[column].unique()

    def __clear_string_from_garbage(self, strr: str) -> str:
        for char in string.punctuation:
            strr = strr.replace(char,"")

        return strr

    def clear_list_of_strings_from_garbage(self, strings: list) -> list:
        response = []

        for strr in strings:
            response.append(self.__clear_string_from_garbage(strr))
        
        return response
        
