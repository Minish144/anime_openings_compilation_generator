from api.openingsdb import OpeningsDB

class OpeningsMoe(OpeningsDB):
    def init_url(self):
        self.api_url = "https://openings.moe/api/list.php"