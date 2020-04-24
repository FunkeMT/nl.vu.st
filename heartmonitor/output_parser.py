from entity import StatusEnum, MeasurementResult, Measurement
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
    switcher = {
        StatusEnum.OK: colors.GREEN,
        StatusEnum.MISSING: colors.BLUE,
        StatusEnum.MAJOR: colors.ORANGE,
        StatusEnum.MINOR: colors.YELLOW,
        StatusEnum.LIFE_THREATENING: colors.RED,
    }
    return switcher.get(status)


def print_status(mr: MeasurementResult):
    post_status = colors.ENDC

    print(f"[%s]" % (datetime.now().strftime("%d-%m-%y %H:%M:%S")), end=" ")
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
    print(
        f"SaO2: %d %%, status: %s%s%s"
        % (
            mr.m.oxygen,
            get_severity_color(mr.oxygen_status),
            mr.oxygen_status.value,
            post_status,
        ),
        end=" | ",
    )
    print(
        f"Blood pressure %d/%d mm Hg, Systolic status: %s%s%s, Diastolic status: %s%s%s"
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
