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
        
    def __get_random_songs(self) -> flask.wrappers.Response:
        count: int = int(flask.request.args.get('count'))
        song_type: int = int(flask.request.args.get('type'))

        if not song_type:
            song_type = 3

        title: str = flask.request.args.get('title')

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
            
        titile_list = self.facade.get_songs_by_title(title=anime_title.lower(),
                                                    exact=exact)

        return flask.jsonify(titile_list)

    def __set_routes(self) -> None:
        self.__get_op = self.session.route('/api/songs/random')(self.__get_random_songs)
        self.__get_songs = self.session.route('/api/songs/anime/<anime_title>')(self.__get_song_list_by_title)

    def run(self, host: str = '0.0.0.0', port: str = '5000') -> None:
        self.session.run(host=host, 
                        port=port)
