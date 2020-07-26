import dotenv
import logging
import os

from server.server import Server

dotenv.load_dotenv()

server = Server(__name__)

app = server.session

if __name__ == '__main__':
	server.run(host=os.getenv('SERVER_HOST'), 
		   port=os.getenv('SERVER_PORT'))
