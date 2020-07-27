import pandas as pd
from fuzzywuzzy import fuzz
import string
import re
class Utils():
    def __init__(self):
        pass

    def __clear_string_from_garbage(self, strr: str) -> str:
        for char in string.punctuation:
            strr = strr.replace(char,"")

        strr = re.sub(r'\s+', ' ', strr)

        return strr

    def __clear_list_of_strings_from_garbage(self, strings: list) -> list:
        response = []

        for strr in strings:
            response.append(self.__clear_string_from_garbage(strr))
        
        return response

    def find_simillar(self, lst: list, req: str):
        response_list = []

        req = self.__clear_string_from_garbage(req)
        lst = self.__clear_list_of_strings_from_garbage(lst)

        for elem in lst:
            if req in elem:
                response_list.append(elem)
            elif fuzz.ratio(elem, req) > 75:
                response_list.append(elem)
        
        return response_list

    def get_unique_names(self, df: pd.DataFrame, column: str) -> list:
        return df[column].unique()
        
