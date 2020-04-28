from entity import (
    StatusEnum,
    MeasurementResult,
    Measurement,
    MeasurementStatistics,
    Statistics,
)
from datetime import datetime
import entity

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
    print_measurement_statistics(s.pulse)
    print(f"Oxygen statistics: \t\t", end="")
    print_measurement_statistics(s.oxygen)
    print(f"Blood pressure systolic statistics: \t", end="")
    print_measurement_statistics(s.blood_pressure_systolic)
    print(f"Blood pressure diastolic statistics: \t", end="")
    print_measurement_statistics(s.blood_pressure_diastolic)
    print(f"Simulation finished: \t")


def print_measurement_statistics(ms: MeasurementStatistics):
    """
    Prints a MeasuremenStatistics object with color for status
    
    :param: ms: MeasurementStatistics object

    """

    if ms.ok_count < 10:
        print(
            f"[{colors.GREEN}OK{colors.ENDC}: {ms.ok_count};\t\t {colors.BLUE}MISSING{colors.ENDC}: {ms.missing_count};\t {colors.YELLOW}MINOR{colors.ENDC}:{ms.minor_count};\t {colors.ORANGE} MAJOR{colors.ENDC}: {ms.major_count};\t {colors.RED} LIFE_THREATENING{colors.ENDC}: {ms.life_threatening_count}\t]"
        )
    else:
        print(
            f"[{colors.GREEN}OK{colors.ENDC}: {ms.ok_count};\t {colors.BLUE}MISSING{colors.ENDC}: {ms.missing_count};\t {colors.YELLOW}MINOR{colors.ENDC}:{ms.minor_count};\t {colors.ORANGE} MAJOR{colors.ENDC}: {ms.major_count};\t {colors.RED} LIFE_THREATENING{colors.ENDC}: {ms.life_threatening_count}\t]"
        )


def print_status(mr: MeasurementResult):
    """
    Prints measurement results

    "param" mr: MeasurementResult object

    """
    post_status = colors.ENDC

    print(f"[%s]" % (datetime.now().strftime("%d-%m-%y %H:%M:%S")), end=" ")
    pulse = mr.m.pulse
    oxygen = mr.m.oxygen
    blood_pressure_diastolic = mr.m.blood_pressure_diastolic
    blood_pressure_systolic = mr.m.blood_pressure_systolic

    if mr.pulse_status == entity.StatusEnum.MISSING:
        pulse = 0
    if mr.oxygen_status == entity.StatusEnum.MISSING:
        oxygen = 0
    if mr.blood_pressure_systolic_status == entity.StatusEnum.MISSING:
        blood_pressure_systolic = 0
    if mr.blood_pressure_diastolic_status == entity.StatusEnum.MISSING:
        blood_pressure_diastolic = 0
    print(
        f"Pulse: %d bpm, status: %s%s%s"
        % (
            pulse,
            get_severity_color(mr.pulse_status),
            mr.pulse_status.value,
            post_status,
        ),
        end=" | ",
    )
    print(
        f"SaO2: %d %%, status: %s%s%s"
        % (
            oxygen,
            get_severity_color(mr.oxygen_status),
            mr.oxygen_status.value,
            post_status,
        ),
        end=" | ",
    )
    print(
        f"Blood pressure %d/%d mm Hg, Systolic status: %s%s%s, Diastolic status: %s%s%s"
        % (
            blood_pressure_systolic,
            blood_pressure_diastolic,
            get_severity_color(mr.blood_pressure_systolic_status),
            mr.blood_pressure_systolic_status.value,
            post_status,
            get_severity_color(mr.blood_pressure_diastolic_status),
            mr.blood_pressure_diastolic_status.value,
            post_status,
        )
    )
