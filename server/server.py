import flask
import flask_cors

from logic.facade import Facade
from utils.utils import Utils

class Server:
    def __init__(self, import_name: str) -> None:
        self.session: flask.Flask = flask.Flask(import_name)
        flask_cors.CORS(self.session)

        self.facade = Facade()
        self.utils = Utils()
        self.__set_routes()

        print('Success!')
        
    def __get_songs(self) -> flask.wrappers.Response:
        random = flask.request.args.get('random')
        random = False if not random else self.utils.str_to_bool(random)
        

        count = flask.request.args.get('count')
        count = int(count) if count else 9999
        
        song_type = flask.request.args.get('type')
        song_type = int(song_type) if song_type else 4
        
        title: str = flask.request.args.get('title')
        
        if not random:
            response = self.facade.get_list_of_animes(count=count,
                                                    song_type=song_type)
        else:
            if title:
                response = self.facade.get_random_webms_by_anime_title(count=count,
                                                        title=title,
                                                        song_type=song_type)
            else:
                response = self.facade.get_random_webms(count=count, 
                                                        song_type=song_type)

        return flask.jsonify(response)

    def __get_song_list_by_title(self, anime_title: str) -> flask.wrappers.Response:
        exact = flask.request.args.get('exact')
        exact = False if not exact else self.utils.str_to_bool(exact)
        print(exact)
        titles_list = self.facade.get_songs_by_title(title=anime_title.lower(),
                                                    exact=exact)

        return flask.jsonify(titles_list)


    def __set_routes(self) -> None:
        self.__api_songs = self.session.route('/api/songs')(self.__get_songs)
        self.__api_songs_anime = self.session.route('/api/songs/<anime_title>')(self.__get_song_list_by_title)
        self.__get_anime_list = None

    def run(self, host: str = '0.0.0.0', port: str = '5000') -> None:
        self.session.run(host=host, 
                        port=port)
