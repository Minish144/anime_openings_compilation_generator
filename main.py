import dotenv
import logging
import os

import config
from utils.filemanager import FileManager
from server.server import Server


def main():
    dotenv.load_dotenv()

    FileManager.make_dir(config.logs.LOGS_PATH)
    logging.basicConfig(filename=config.logs.LOGS_FILE_PATH,
                        filemode='w',
                        level=config.logs.LOGS_LEVEL)

    server = Server(__name__)
    server.run(host=os.getenv('SERVER_HOST'),
               port=os.getenv('SERVER_PORT'))


if __name__ == '__main__':
    main()
