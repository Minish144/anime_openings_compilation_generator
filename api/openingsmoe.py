from api.openingsdb import OpeningsDB
import pandas as pd

class OpeningsMoe(OpeningsDB):
    def init_url(self):
        self.api_url = "https://openings.moe/api/list.php"
    
    def __song_type_upd(self, x: str) -> str:
        x = x.replace(' ', '')
        x = x.replace('Opening', 'OP')
        x = x.replace('Ending', 'ED')
        return x

    def process_dataset(self):
        self.op_list['file'] = self.op_list['file'].apply(lambda x: f'https://openings.moe/video/{x}.webm')    

        self.op_list['Song_Title'] = self.op_list['song'].apply(lambda x: x['title'] if type(x) == dict else None)
        self.op_list['Song_Artist'] = self.op_list['song'].apply(lambda x: x['artist'] if type(x) == dict else None) 

        self.op_list['Song_Artist'] = self.op_list['Song_Artist'].apply(lambda x: None if x == 'NO NAME' else x)

        self.op_list.drop(columns=['mime', 'subtitles', 'song'], inplace=True)

        self.op_list.rename(columns={
                    'title':'Song_Type',
                    'source':'Anime_Title',
                    'file':'Video_URL',
                    },
                    inplace=True)
        
        self.op_list = self.op_list.where(pd.notnull(self.op_list), None)

        self.op_list['Song_Type'] = self.op_list['Song_Type'].apply(lambda x: self.__song_type_upd(x))
        self.op_list['Video_URL'] = self.op_list['Video_URL'].str.replace('：', '%EF%BC%9A')
        self.op_list = self.op_list.reindex(columns=['Anime_Title', 'Song_Artist', 'Song_Title', 'Song_Type', 'Video_URL'])