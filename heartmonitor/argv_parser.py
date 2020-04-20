from typing import List

def parse(argv: List[str], key: str):
    """
    :param: argv: Commandline arguments.
    :param: key: Key to find in the commandline arguments.
    :return: Value of the commandline argument.
    """
    if key not in argv:
        raise NameError

    keyIndex = argv.index(key)
    valueIndex = keyIndex + 1
    if valueIndex >= len(argv):
        raise ValueError
    return argv[valueIndex]
