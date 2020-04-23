import argv_parser, entity
import sys
from typing import List


def print_help():
    """
    Print help message.
    """
    print("Command usage is as follows:")
    print("heartbeatmonitor.py arguments:")
    print("")
    print("Arguments are the following:")

def main(argv: List[str]):
    patient = None # type: entity.Patient
    try:
        patient = get_patient_information(argv)
    except:
        print_help()
        sys.exit(1)

        

    

if __name__ == "__main__":
    main(sys.argv)