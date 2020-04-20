from typing import List, Dict

def parse(argv: List[str], key: str) -> str:
    """
    Parses argv commands for key value pair.

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


def parse_multiple(argv: List[str], keys: List[str]) -> Dict[str, str]:
    """
    Parses argv commands for key value pairs.

    :param: argv: Commandline arguments.
    :param: keys: Keys to find in the commandline arguments.
    :return: Per key the value of the commandline argument.
    :raises: NameError When key was not found.
    :raises: ValueError When value was not found after key.
    """
    res = {}
    for key in keys:
        res[key] = parse(argv, key)

    return res

