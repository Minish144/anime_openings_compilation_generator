import requests
import pandas as pd
from typing import Union

class OpeningsDB():
    def __init__(self):
        self.init_url()
        self.set_dataset()
        self.process_dataset()

    def init_url(self):
        self.api_url = "https://openings.moe/api/list.php"

    def get_op_list(self) -> list:
        url = self.api_url
        response = requests.get(url)
        op_list = response.json()
        return op_list
    
    def set_dataset(self) -> None:
        op_list = self.get_op_list()
        self.op_list = pd.DataFrame(op_list)

    def process_dataset(self) -> None:
        pass

    def get_openings_list(self, count: Union[int, None] = None) -> None:
       return self.op_list if count == None else self.op_list.head(count)