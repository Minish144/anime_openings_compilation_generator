from api.openingsdb import OpeningsDB

class AnimeThemes(OpeningsDB):
    def init_url(self):
        self.api_url = "https://raw.githubusercontent.com/xLasercut/anime-music-quiz/master/server/data/song-list.json"