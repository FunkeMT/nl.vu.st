import argv_parser, entity, processor, output_parser, logger
import sys
from typing import List
import time

MEASUREMENT_INTERVAL_IN_MS = 1000
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
    try:
        recording = None  # type: entity.FileRecording
        try:
            recording = entity.FileRecording(csv_location).get_iterator()
        except:
            print_help()
            sys.exit(1)

        while True:
            m = None  # type: entity.Measurement
            try:
                m = recording.__next__(make_invalid_measurement_missing=True)
            except StopIteration:
                break

    for m in entity.FileRecording(csv_location).get_iterator():
        measurement_results = processor.processing_agent(m, statistics)
        measurement_string = output_parser.format_status(measurement_results)
        print(measurement_string, , flush=True)
        logger.log(measurement_string)
        number_of_measurements += 1
        wait_on_new_measurement()
    stat_string = output_parser.format_statistics(statistics)
    print(stat_string, , flush=True)
    logger.log(stat_string)
    message_done = "Processed {nom} measurements".format(nom=number_of_measurements)
    logger.log(message_done)
    print(f"Processed {number_of_measurements} measurements")


if __name__ == "__main__":
    main(sys.argv)
