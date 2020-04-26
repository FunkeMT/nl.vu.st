import argv_parser, entity, processor, output_parser
import sys
from typing import List
import time

MEASUREMENT_INTERVAL_IN_MS = 500
MILLISECONDS_IN_SECOND = 1000


def wait_on_new_measurement():
    """
    Wait until new measurement has been made.

    :raises: KeyboardInterrupt When some tried to stop the application.
    :raises: Exception When a thread error occured.
    """
    time.sleep(MEASUREMENT_INTERVAL_IN_MS / MILLISECONDS_IN_SECOND)


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
    csv_location = None  # type: str
    try:
        csv_location = argv_parser.parse(argv, "--path")
    except:
        print_help()
        sys.exit(1)

    # Create statistics
    oxygen_ms = entity.MeasurementStatistics()
    pulse_ms = entity.MeasurementStatistics()
    blood_pressure_systolic_ms = entity.MeasurementStatistics()
    blood_pressure_diastolic_ms = entity.MeasurementStatistics()
    statistics = entity.Statistics(
        oxygen_ms, pulse_ms, blood_pressure_systolic_ms, blood_pressure_diastolic_ms
    )

    number_of_measurements = 0

    for m in entity.FileRecording(csv_location).get_iterator():
        measurement_results = processor.processing_agent(
            m, statistics
        )  # add other measurements statistics here
        output_parser.print_status(measurement_results)
        # print("RESULT FOR OXYGEN", measurement_results.oxygen_status)
        # print("RESULT FOR SYSBP", measurement_results.blood_pressure_systolic_status)
        # print("RESULT FOR DIABP", measurement_results.blood_pressure_diastolic_status)
        number_of_measurements += 1
        wait_on_new_measurement()


if __name__ == "__main__":
    main(sys.argv)
