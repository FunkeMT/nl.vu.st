import argv_parser
import sys
import entity
from typing import List

def get_patient_information(argv: List[str]) -> entity.Patient:
    """
    Get patient information from argv.

    :param: argv: Argv to look into.
    :return: Patient filled with commandline information.
    :raises: NameError When key was not found.
    :raises: ValueError When value was not found after key.
    """
    # a = argv_parser.parse_multiple(sys.argv, ["--age", "--height", "--weight", "--gender"])
    pass

if __name__ == "__main__":
    print("hey")
