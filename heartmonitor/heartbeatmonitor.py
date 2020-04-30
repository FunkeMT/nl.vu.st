import argv_parser, entity, processor, output_parser, logger
import sys
from typing import List
import time
import signal
from threading import Lock

MEASUREMENT_INTERVAL_IN_MS = 1000
MILLISECONDS_IN_SECOND = 1000

help_message_shown_lock = Lock()
help_message_shown = False
handled_signal_handler = False

def wait_on_new_measurement():
    """
    Wait until new measurement has been made.

    :raises: KeyboardInterrupt When some tried to stop the application.
    :raises: Exception When a thread error occured.
    """
    for _ in range(0, MEASUREMENT_INTERVAL_IN_MS):
        time.sleep(1 / MILLISECONDS_IN_SECOND)


def print_help():
    """
    Print help message.
    """
    global help_message_shown
    global help_message_shown_lock

    help_message_shown_lock.acquire()

    if help_message_shown:
        help_message_shown_lock.release()
        return

    help_message_shown = True

    print("Usage: heartbeatmonitor.py [options] file")
    print("Options:")
    print("\t--path")
    print("")
    print(
        "The system will generate a status for each measurement, these statuses should be interpreted as follows:"
    )
    print("OK:               A reading that is not considered dangerous.")
    print("MISSING:          A reading that is not considered a valid reading.")
    print(
        "MINOR:            A reading that is of interest to medical personnel but cannot be considered a threat yet."
    )
    print(
        "MAJOR:            A reading that is of interest to medical personnel and has to be considered a threat."
    )
    print(
        "LIFE_THREATENING: A reading that is of interest to medical personnel because it can have severe effects on the chance of survival of the patient."
    )
    help_message_shown_lock.release()


def signal_handler(sig, frame):  # pragma: no mutate
    global handled_signal_handler
    if handled_signal_handler: return
    handled_signal_handler = True
    print_help()
    sys.exit(1)


def main(argv: List[str]):
    csv_location = None  # type: str
    try:
        csv_location = argv_parser.parse(argv, "--path")
    except:
        print_help()
        sys.exit(1)
        return

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
            return

        while True:
            m = None  # type: entity.Measurement
            try:
                m = recording.__next__(make_invalid_measurement_missing=True)
            except StopIteration:
                break

            measurement_results = processor.processing_agent(m, statistics)
            result_string = output_parser.format_status(measurement_results)
            print(result_string, flush=True)
            logger.log(result_string)
            number_of_measurements += 1
            wait_on_new_measurement()
    except KeyboardInterrupt:
        # When someone wants to stop the program prematurely.
        pass
    statistics_string = output_parser.format_statistics(statistics)
    print(statistics_string, flush=True)
    logger.log(statistics_string)
    print(f"Processed {number_of_measurements} measurements")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main(sys.argv)
