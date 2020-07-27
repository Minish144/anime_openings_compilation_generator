import flask
import flask_cors

from logic.facade import Facade

class Server:
    def __init__(self, import_name: str) -> None:
        self.session: flask.Flask = flask.Flask(import_name)
        flask_cors.CORS(self.session)

        self.facade = Facade()

        self.__set_routes()

        print('Success!')
        
    def __get_random_songs(self) -> flask.wrappers.Response:
        count: int = int(flask.request.args.get('count'))
        
        song_type: int = int(flask.request.args.get('type'))
        if not song_type:
            song_type = 3

        title: str = str(flask.request.args.get('title'))

        if title:
            print('yes', title)
            response = self.facade.get_random_webms_by_anime_title(count=count,
                                                    title=title,
                                                    song_type=song_type)
        else:
            print('not yes')
            response = self.facade.get_random_webms(count=count, 
                                                    song_type=song_type)

        return flask.jsonify(response)

    def __set_routes(self) -> None:
        self.__get_op = self.session.route('/api/songs/random')(self.__get_random_songs)
        
    def run(self, host: str = '0.0.0.0', port: str = '5000') -> None:
        self.session.run(host=host, port=port)
