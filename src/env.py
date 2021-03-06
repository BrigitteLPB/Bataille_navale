#conding:utf-8

from io import StringIO
from json import loads
from pathlib import Path
from os import environ
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
        # _ = load_dotenv(stream=StringIO(f"ROOT_PATH={Path(__file__).parent.resolve()}"))
        # _ = load_dotenv(stream=StringIO(f"ENV_FILE_PATH={(Path(EnvUtilServer.env['SERVER_ROOT_PATH']) / '.env').resolve()}"))
        # _ = load_dotenv(dotenv_path=EnvUtilServer.env['SERVER_ENV_FILE_PATH'], override=True)
        pass

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
