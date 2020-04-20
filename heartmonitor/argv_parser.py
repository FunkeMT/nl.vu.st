from typing import List

def parse(argv: List[str], key: str):
    """
    :param: argv: Commandline arguments.
    :param: key: Key to find in the commandline arguments.
    :return: Value of the commandline argument.
    :raises: NameError When key was not found.
    :raises: ValueError When value was not found after key.
    """
    if key not in argv:
        raise NameError

    keyIndex = argv.index(key)
    valueIndex = keyIndex + 1
    if valueIndex >= len(argv):
        raise ValueError
    return argv[valueIndex]
