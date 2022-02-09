
from enum import Enum
from datetime import datetime
from pathlib import Path
from env import EnvUtilServer

class LogState(str, Enum):
    """Enum for Log State
    """
    INFO    =   'info'
    WARNING =   'warning'
    ERROR   =   'error'
    DEBUG   =   'debug'


class LogUtil:
    """this class groups up all the function for log actions
    """

    @staticmethod
    def log(log_state: LogState, log_message: str):
        """generic function for logging in console and file
        Args:
            logState (LogState): state of the log field (error, info, warn, debug, ...)
            logMessage (str): logged message
        """
        now = datetime.now().astimezone()

        # console
        LogUtil.log_console(log_state, log_message, now)

        # log file
        LogUtil.log_file(log_state, log_message, now)


    @staticmethod
    def log_console(log_state: LogState, log_message: str, now: datetime):
        """log the message on console
        Args:
            logType (LogState): state of the log field (error, info, warn, debug, ...)
            logMessage (str): logged message
            now (datetime): showed date in the log field
        """
        print(f"{'['+str(log_state.value).upper()+']':<10} #{now.strftime('%Y-%m-%d %I:%M:%S')} >\t{log_message}")

    @staticmethod
    def log_file(log_state: LogState, log_message: str, now: datetime, ):
        """log the message in file
        Args:
            logType (LogState): state of the log field (error, info, warn, debug, ...)
            logMessage (str): logged message
            now (datetime): showed date in the log field
        """
        try:
            path = EnvUtilServer.env['LOG_FOLDER']
            if path != '' :
                # filepath = (Path(EnvUtilServer.env['ROOT_PATH']) / Path(path) / ('SERVER_' + now.strftime("%Y-%m-%d") + ".log")).resolve()
                filepath = (Path(EnvUtilServer.env['LOG_FOLDER']) / Path(path) / ('' + now.strftime("%Y-%m-%d") + ".log")).resolve()

                # making the folder
                for folder in reversed(filepath.parents):
                    Path(str(folder)).mkdir(exist_ok=True)

                # creating file
                filepath.touch()
                file = open(str(filepath), 'a', encoding='utf-8')
                _ = file.write(f"{'['+str(log_state.value).upper()+']':<10} {now.strftime('%Y-%m-%d %I:%M:%S')} >\t{log_message}\n")
        except KeyError as key_error:
            LogUtil.log_console(LogState.ERROR, f"No path to log folder found: {key_error.args[0]}", now)            
        except FileExistsError as file_error:
            LogUtil.log_console(LogState.ERROR, f"no file found to write log : {file_error.args}", now)
       
   
    @staticmethod
    def INFO(message: str):
        LogUtil.log(LogState.INFO, message)

    @staticmethod
    def WARN(message: str):
        LogUtil.log(LogState.WARNING, message)

    @staticmethod
    def ERROR(message: str):
        LogUtil.log(LogState.ERROR, message)

    @staticmethod
    def DEBUG(message: str):
        LogUtil.log(LogState.DEBUG, message)


if __name__ == "__main__":
    EnvUtilServer.new()

    LogUtil.log(LogState.INFO, "test de log")
    LogUtil.log(LogState.WARNING, "test de log")
    LogUtil.log(LogState.ERROR, "test de log")
    LogUtil.log(LogState.DEBUG, "test de log")