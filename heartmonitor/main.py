import argv_parser, entity, processor
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
    print("  --path str\tLocation of the CSV file")


def main(argv: List[str]):
    csv_location = None # type: str
    try:
        csv_location = argv_parser.parse(argv, "--path")
    except:
        print_help()
        sys.exit(1)
    
    oxygen_ms = entity.MeasurementStatistics() # add other measurements statistics here
    number_of_measurements = 0

    for m in entity.FileRecording(csv_location).get_iterator():
        print(m.__dict__)
        status = processor.processing_agent(m, [oxygen_ms]) # add other measurements statistics here

        number_of_measurements += 1

    print("OXYGEN", oxygen_ms.__dict__)


if __name__ == "__main__":
    main(sys.argv)