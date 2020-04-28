from entity import (
    StatusEnum,
    MeasurementResult,
    Measurement,
    MeasurementStatistics,
    Statistics,
)
from datetime import datetime


class colors:
    PURPLE = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    ORANGE = "\033[33m"
    RED = "\033[91m"
    ENDC = "\033[0m"


def get_severity_color(status: StatusEnum):
    """
    Returns color according to severity of the threat
    
    :param: status: Status of a value
    :return: color according to status
    """
    switcher = {
        StatusEnum.OK: colors.GREEN,
        StatusEnum.MISSING: colors.BLUE,
        StatusEnum.MAJOR: colors.ORANGE,
        StatusEnum.MINOR: colors.YELLOW,
        StatusEnum.LIFE_THREATENING: colors.RED,
    }
    return switcher.get(status)


def print_statistics(s: Statistics):
    """
    Prints the statistics with color for status
    
    :param: s: statistics object

    """
    print(f"Pulse statistics: \t\t", end="")
    pulsestring = "Pulse statistics: \t\t"
    pulsecontent = print_measurement_statistics(s.pulse)
    print(f"Oxygen statistics: \t\t", end="")
    oxygenstring = "Oxygen statistics: \t\t"
    oxygencontent = print_measurement_statistics(s.oxygen)
    print(f"Blood pressure systolic statistics: \t", end="")
    systolicstring = "Blood pressure systolic statistics: \t"
    systoliccontent = print_measurement_statistics(s.blood_pressure_systolic)
    print(f"Blood pressure diastolic statistics: \t", end="")
    diastolicstring = "Blood pressure diastolic statistics: \t"
    diastoliccontent = print_measurement_statistics(s.blood_pressure_diastolic)
    print(f"Simulation finished: \t", end="")
    finishedstring = "Simulation Finished: \t"

    statisticsstring = (
        pulsestring
        + pulsecontent
        + "\n"
        + oxygenstring
        + oxygencontent
        + "\n"
        + systolicstring
        + systoliccontent
        + "\n"
        + diastolicstring
        + diastoliccontent
        + "\n"
        + finishedstring
    )
    return statisticsstring


def print_measurement_statistics(ms: MeasurementStatistics) -> str:
    """
    Prints a MeasuremenStatistics object with color for status
    
    :param: ms: MeasurementStatistics object

    """
    statisticsstring = "[OK: {ok};\t\tMISSING: {missing};\t\tMINOR: {minor};\t\tMAJOR: {major};\t\tLIFE_THREATENING: {lt}]".format(
        ok=ms.ok_count,
        missing=ms.missing_count,
        minor=ms.minor_count,
        major=ms.major_count,
        lt=ms.life_threatening_count,
    )

    print(
        f"[{colors.GREEN}OK{colors.ENDC}: {ms.ok_count};\t\t{colors.BLUE}MISSING{colors.ENDC}: {ms.missing_count};\t{colors.YELLOW}MINOR{colors.ENDC}:{ms.minor_count};\t {colors.ORANGE} MAJOR{colors.ENDC}: {ms.major_count};\t {colors.RED} LIFE_THREATENING{colors.ENDC}: {ms.life_threatening_count}\t]"
    )

    return statisticsstring


def print_status(mr: MeasurementResult) -> str:
    """
    Prints measurement results

    "param" mr: MeasurementResult object
    "return" the string that is printed to the screen

    """
    post_status = colors.ENDC

    now = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    datestring = "[{time}]".format(time=now)
    print(f"{datestring}", end=" ")
    pulsestring = "Pulse: {pulse} bpm, status: {pulse_status}".format(
        pulse=mr.m.pulse, pulse_status=mr.pulse_status.value
    )
    print(
        f"Pulse: %d bpm, status: %s%s%s"
        % (
            mr.m.pulse,
            get_severity_color(mr.pulse_status),
            mr.pulse_status.value,
            post_status,
        ),
        end=" | ",
    )
    oxygenstring = "SaO2: {oxygen}% status: {oxygen_status}".format(
        oxygen=mr.m.oxygen, oxygen_status=mr.oxygen_status.value
    )
    print(
        f"SaO2: %d%%, status: %s%s%s"
        % (
            mr.m.oxygen,
            get_severity_color(mr.oxygen_status),
            mr.oxygen_status.value,
            post_status,
        ),
        end=" | ",
    )
    bloodpressurestring = "Blood pressure: {systolic}/{diastolic} mm Hg, Systolic status: {systolic_status}, Diastolic status: {diastolic_status}".format(
        systolic=mr.m.blood_pressure_systolic,
        diastolic=mr.m.blood_pressure_diastolic,
        systolic_status=mr.blood_pressure_systolic_status.value,
        diastolic_status=mr.blood_pressure_diastolic_status.value,
    )

    print(
        f"Blood pressure: %d/%d mm Hg, Systolic status: %s%s%s, Diastolic status: %s%s%s"
        % (
            mr.m.blood_pressure_systolic,
            mr.m.blood_pressure_diastolic,
            get_severity_color(mr.blood_pressure_systolic_status),
            mr.blood_pressure_systolic_status.value,
            post_status,
            get_severity_color(mr.blood_pressure_diastolic_status),
            mr.blood_pressure_diastolic_status.value,
            post_status,
        )
    )

    return (
        datestring
        + " | "
        + pulsestring
        + " | "
        + oxygenstring
        + " | "
        + bloodpressurestring
        + "\n"
    )
