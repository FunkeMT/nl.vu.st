from datetime import datetime
import sys, os, errno, pathlib

LOG_FOLDER_NAME = str(pathlib.Path(__file__).parent.absolute()) + os.path.sep + "logs"
no_logs = False


def log(message: str):
    """
    Writes a string in the log file
    Creates a logfile folder if this does not exists
    Creates a log for the current date if this does not exist

    :param: message: message string to be written
    :raises: IOError if the system is out of space
    :raises: IOError if the system does not have permission to write
    """
    global no_logs
    if no_logs == True:
        return
    if not os.path.exists(LOG_FOLDER_NAME):
        try:
            os.makedirs(LOG_FOLDER_NAME)
        except IOError as e:
            log_error(e)  # pragma: no mutate
    date = datetime.now().strftime("%d-%m-%y")
    logfilename = LOG_FOLDER_NAME + os.path.sep + date
    writemode = "w"
    if os.path.exists(logfilename):
        writemode = "a"
    try:
        logfile = open(logfilename, writemode)
        logfile.write(message + os.linesep)
        logfile.close()
    except IOError as e:
        log_error(e)


def log_error(e: errno):
    global no_logs
    if e.errno == errno.ENOSPC:
        print("No space left on device to create logs!")
        no_logs = True
    elif e.errno == errno.EACCES:
        print("No permission to create logs!")
        no_logs = True
