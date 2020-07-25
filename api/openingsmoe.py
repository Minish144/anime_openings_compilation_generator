from api.openingsdb import OpeningsDB

class OpeningsMoe(OpeningsDB):
    def init_url(self):
        self.api_url = "https://openings.moe/api/list.php"
    
    def process_dataset(self):
        self.op_list['file'] = self.op_list['file'].apply(lambda x: f'https://openings.moe/video/{x}.webm')