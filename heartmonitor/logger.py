from datetime import datetime
import sys, os

LOGFOLDERNAME = "logs"


def log(s: str):
    """
    Writes a string in the log file
    Creates a logfile folder if this does not exists
    Creates a log for the current date if this does not exist

    :param: s: String to be written
    """
    if not os.path.exists(LOGFOLDERNAME):
        os.makedirs(LOGFOLDERNAME)

    date = datetime.now().strftime("%d-%m-%y")
    if os.path.exists(LOGFOLDERNAME + "/" + date):
        writemode = "a"
    else:
        writemode = "w"
    logfile = open(LOGFOLDERNAME + "/" + date, writemode)
    logfile.write(s)
