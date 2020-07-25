from api.openingsdb import OpeningsDB

class AnimeThemes(OpeningsDB):
    def init_url(self):
        self.api_url = "https://raw.githubusercontent.com/xLasercut/anime-music-quiz/master/server/data/song-list.json"

    def process_dataset(self):
        self.op_list = self.op_list.drop(columns=['songId'])
        self.op_list.rename(columns={
                            'anime':'Anime_Title',
                            'src':'Video_URL',
                            'title':'Song_Title',
                            'artist':'Song_Artist',
                            'type':'Song_Type',
                          },
                          inplace=True)
        self.op_list['Anime_Title'] = self.op_list['Anime_Title'].apply(lambda x: x[0])