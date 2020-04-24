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

    #Create statistics
    oxygen_ms = entity.MeasurementStatistics()
    pulse_ms = entity.MeasurementStatistics()
    blood_pressure_systolic = entity.MeasurementStatistics()
    blood_pressure_diastolic = entity.MeasurementStatistics()
    statistics = entity.Statistics(oxygen_ms, pulse_ms, blood_pressure_systolic, blood_pressure_diastolic)
    
    number_of_measurements = 0

    for m in entity.FileRecording(csv_location).get_iterator():
        print(m.__dict__)
        measurement_results = processor.processing_agent(m, statistics) # add other measurements statistics here
        print("RESULT FOR OXYGEN", measurement_results.oxygen_status)
        number_of_measurements += 1




if __name__ == "__main__":
    main(sys.argv)