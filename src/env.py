#conding:utf-8

from json import loads
from os import environ
from io import StringIO
from pathlib import Path
from pickle import NONE
from dotenv import load_dotenv


ENV_INIT = False


class EnvUtilServer() :
    """group up the function for the env
    """

    env = environ

    @staticmethod
    def new():
        """load the env variable
        """
        try:
            _ = EnvUtilServer.env['ASSETS_FOLDER']
        except KeyError:
            _ = load_dotenv(stream=StringIO(f"ROOT_PATH={Path(__file__).parent.resolve()}"))
            _ = load_dotenv(stream=StringIO(f"ASSETS_FOLDER={(Path(EnvUtilServer.env['ROOT_PATH']) / 'assets').resolve()}"))
        EnvUtilServer.env = environ

    @staticmethod
    def to_bool(env_value: str):
        return loads(env_value.lower())


# if not ENV_INIT :
#     ENV_INIT = True
#     EnvUtilServer.new()


if __name__ == "__main__":
    EnvUtilServer.new()
    
    print(EnvUtilServer.env)
    print(f"ROOT_PATH={EnvUtilServer.env['ROOT_PATH']}")
    print(f"ENV_FILE_PATH={EnvUtilServer.env['ENV_FILE_PATH']}")
    print(f"LOG_FOLDER={EnvUtilServer.env['LOG_FOLDER']}")