import pandas as pd
from fuzzywuzzy import fuzz
import string
import re

class Utils():
    def __init__(self):
        pass

    def __clear_string_from_garbage(self, strr: str) -> str:
        for char in string.punctuation:
            strr = strr.replace(char," ")

        strr = re.sub(r'\s+', ' ', strr)
        strr = strr.lower()
        return strr

    def __clear_list_of_strings_from_garbage(self, strings: list) -> list:
        response = []

        for strr in strings:
            response.append(self.__clear_string_from_garbage(strr))
        
        return response

    def find_simillar(self, lst: list, req: str):
        response_list = []
        clr = self.__clear_string_from_garbage

        req = self.__clear_string_from_garbage(req)

        for elem in lst:
            elem_clrd = clr(elem)
            if elem_clrd.find(req) != -1:
                response_list.append(elem)  
            elif fuzz.ratio(elem_clrd, req) > 75:
                response_list.append(elem)
        
        return response_list

    def get_unique_names(self, df: pd.DataFrame, column: str) -> list:
        return df[column].unique()

    def str_to_bool(self, value: str) -> bool:
        return value.lower() in ("true", "yes", "t", "1")