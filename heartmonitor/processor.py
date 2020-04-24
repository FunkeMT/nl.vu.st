import entity
from typing import List


def processing_agent(measurement: entity.Measurement, statistics: entity.Statistics):
    """
    The processing agent goes through the whole measurement. 
    For the types (oxygen, pulse, and both bloodpressures) 
    	- they will be analyised for validity and status
    	- their status will be added to their measurement statistics
    	- they will be added to the measurement results
    those results will be returned to the main
    """
    oxygen_status = oxygen_analysis(measurement.oxygen, statistics.oxygen)
    systolic_status = blood_pressure_systolic_analysis(
        measurement.blood_pressure_systolic, statistics.blood_pressure_systolic
    )
    diastolic_status = blood_pressure_diastolic_analysis(
        measurement.blood_pressure_diastolic, statistics.blood_pressure_diastolic
    )

    # pulse_status = process_pulse(pulse)

    # Add new statuses to the result
    measurement_results = entity.MeasurementResult(
        measurement, oxygen_status, None, systolic_status, diastolic_status
    )

    return measurement_results


def oxygen_analysis(oxygen, measurement_statistics):
    """
    Checks validation and valuation and increment status in statistics of Oxygen
    """
    if not oxygen_validation(oxygen):
        return entity.StatusEnum.MISSING

    status = oxygen_valuation(oxygen)
    measurement_statistics.increment(status)
    return status


def oxygen_validation(oxygen: int):
    """
    Checks if it is an integer and if the number is between -1 and 101
    """
    if not str(oxygen).isnumeric():
        return False

    return int(oxygen) < 101 and int(oxygen) >= 0


def oxygen_valuation(oxygen):
    """
    Checks different values to assign a status to
    """
    if oxygen >= 95:
        return entity.StatusEnum.OK
    elif oxygen >= 90:
        return entity.StatusEnum.MINOR
    elif oxygen > 60:
        return entity.StatusEnum.MAJOR
    elif oxygen <= 60:
        return entity.StatusEnum.LIFE_THREATENING


def process_pulse(pulse):
    # To be implemented
    pass


def blood_pressure_systolic_analysis(blood_pressure_systolic, measurement_statistics):

    if not blood_pressure_systolic_validation(blood_pressure_systolic):
        return entity.StatusEnum.MISSING

    status = blood_pressure_systolic_valuation(blood_pressure_systolic)
    measurement_statistics.increment(status)
    return status


def blood_pressure_systolic_validation(blood_pressure_systolic):

    if not str(blood_pressure_systolic).isnumeric():
        return False

    return int(blood_pressure_systolic) < 251 and int(blood_pressure_systolic) >= 0


def blood_pressure_systolic_valuation(blood_pressure_systolic):
    """
    Checks different values to assign a status to
    """
    if blood_pressure_systolic >= 180:
        return entity.StatusEnum.LIFE_THREATENING
    elif blood_pressure_systolic < 40:
        return entity.StatusEnum.LIFE_THREATENING
    elif blood_pressure_systolic >= 140:
        return entity.StatusEnum.MAJOR
    elif blood_pressure_systolic < 60:
        return entity.StatusEnum.MAJOR
    elif blood_pressure_systolic > 130:
        return entity.StatusEnum.MINOR
    elif blood_pressure_systolic < 90:
        return entity.StatusEnum.MINOR
    elif blood_pressure_systolic <= 129:
        return entity.StatusEnum.OK


def blood_pressure_diastolic_analysis(blood_pressure_diastolic, measurement_statistics):

    if not blood_pressure_diastolic_validation(blood_pressure_diastolic):
        return entity.StatusEnum.MISSING

    status = blood_pressure_diastolic_valuation(blood_pressure_diastolic)
    measurement_statistics.increment(status)
    return status


def blood_pressure_diastolic_validation(blood_pressure_diastolic):

    if not str(blood_pressure_diastolic).isnumeric():
        return False

    return int(blood_pressure_diastolic) < 141 and int(blood_pressure_diastolic) >= 0


def blood_pressure_diastolic_valuation(blood_pressure_diastolic):
    """
    Checks different values to assign a status to
    """
    if blood_pressure_diastolic >= 120:
        return entity.StatusEnum.LIFE_THREATENING
    elif blood_pressure_diastolic < 40:
        return entity.StatusEnum.LIFE_THREATENING
    elif blood_pressure_diastolic >= 90:
        return entity.StatusEnum.MAJOR
    elif blood_pressure_diastolic < 50:
        return entity.StatusEnum.MAJOR
    elif blood_pressure_diastolic > 80:
        return entity.StatusEnum.MINOR
    elif blood_pressure_diastolic < 60:
        return entity.StatusEnum.MINOR
    elif blood_pressure_diastolic <= 80:
        return entity.StatusEnum.OK
