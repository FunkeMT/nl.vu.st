from datetime import datetime
import sys, os


def log(s: str):
    date = datetime.now().strftime("%d-%m-%y")
    if os.path.exists(date):
        writemode = "a"
    else:
        writemode = "w"
    logfile = open(date, writemode)
    logfile.write(s)
