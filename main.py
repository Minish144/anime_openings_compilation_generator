import dotenv
import logging
import os

from server.server import Server

def main():
    dotenv.load_dotenv()

    server = Server(__name__)
    server.run(host=os.getenv('SERVER_HOST'),
               port=os.getenv('SERVER_PORT'))

if __name__ == '__main__':
    main()
