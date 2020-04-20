from heartmonitor import argv_parser, entity
import sys
from typing import List

def get_patient_information(argv: List[str]) -> entity.Patient:
    """
    Get patient information from argv.

    :param: argv: Argv to look into.
    :return: Patient filled with commandline information.
    :raises: NameError When key was not found.
    :raises: ValueError When value was not found after key.
    """

    fields = ["age", "height", "weight", "gender"]
    arguments = ["--" + name for name in fields]
    raw_patient = argv_parser.parse_multiple(argv, arguments)
    obj_arguments = {}

    for field in ["age", "height", "weight"]:
        obj_arguments[field] = int(raw_patient["--" + field])
        if obj_arguments[field] < 0: raise ValueError
    
    gender = raw_patient["--gender"].lower()
    if gender not in ["male", "female"]: raise ValueError

    obj_arguments["gender"] = entity.GenderEnum.MALE
    if gender == "female": obj_arguments["gender"] = entity.GenderEnum.FEMALE

    return entity.Patient(**obj_arguments)
