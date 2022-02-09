#conding:utf-8

from json import loads
from os import environ

ENV_INIT = False


class EnvUtilServer() :
    """group up the function for the env
    """

    env = environ

    @staticmethod
    def new():
        """load the env variable
        """
        env = environ

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