import entity
from typing import List


def processing_agent(
    measurement: entity.Measurement, statistics: entity.Statistics
) -> entity.MeasurementResult:
    """
    The processing agent goes through the whole measurement. 
    For the types (oxygen, pulse, and both bloodpressures) 
    	- they will be analyised for validity and status
    	- their status will be added to their measurement statistics
    	- they will be added to the measurement results
    those results will be returned to the main

    :param: measurement The measurement that will be processed.
    :param: statistics The statistics object that needs to be updated.
    :return: The result of the processing in the form of a results object.
    """
    oxygen_status = oxygen_analysis(measurement.oxygen, statistics.oxygen)
    pulse_status = pulse_analysis(measurement.pulse, statistics.pulse)
    systolic_status = blood_pressure_systolic_analysis(
        measurement.blood_pressure_systolic, statistics.blood_pressure_systolic
    )
    diastolic_status = blood_pressure_diastolic_analysis(
        measurement.blood_pressure_diastolic, statistics.blood_pressure_diastolic
    )

    # Add new statuses to the result
    measurement_results = entity.MeasurementResult(
        measurement, oxygen_status, pulse_status, systolic_status, diastolic_status
    )

    return measurement_results


def oxygen_analysis(
    oxygen: int, measurement_statistics: entity.MeasurementStatistics
) -> entity.StatusEnum:
    """
    Checks validation and valuation and increment status in statistics of
    Oxygen.

    :param: oxygen The oxygen level to analyse.
    :param: measurement_statistics The statistics to update with the analysis.
    :return The result of the analysis.
    """
    status = entity.StatusEnum.MISSING
    if oxygen_validation(oxygen):
        status = oxygen_valuation(oxygen)

    measurement_statistics.increment(status)
    return status


def oxygen_validation(oxygen: int) -> bool:
    """
    Checks if it is an integer and if the number is between -1 and 101.

    :param: oxygen The amount of oxygen to check.
    :return True if a valid value was given.
    """
    if not str(oxygen).isnumeric():
        return False

    return int(oxygen) < 101 and int(oxygen) >= 0


def oxygen_valuation(oxygen: int) -> entity.StatusEnum:
    """
    Checks different values to assign a status to.

    :param: oxygen Oxygen level to evaluate.
    :return Status of the oxygen.
    """
    if oxygen >= 95:
        return entity.StatusEnum.OK
    elif oxygen >= 90:
        return entity.StatusEnum.MINOR
    elif oxygen > 60:
        return entity.StatusEnum.MAJOR
    elif oxygen <= 60:
        return entity.StatusEnum.LIFE_THREATENING


def _pulse_analysis_determine(pulse: int) -> entity.StatusEnum:
    """
    Partly analyses pulse and returns status.
    The status levels are determined as follows (values are inclusive):
     - Min pulse 60, max pulse 100 = OK
     - Min pulse 50, max pulse 120 = MINOR
     - Min pulse 40, max pulse 160 = MAJOR
     - Other values LIFE_THREATENING

    :param: pulse Pulse to be analysed.
    :return Partial status level of the pulse.
    """
    # minimum heart rate: https://thenextchallenge.org/resting-heart-rate/
    # After the age of 10, 60 to 100 is considered normal in a resting
    # position (not including factors such as stress and exercise etc…)
    # https://www.medicalnewstoday.com/articles/235710#target-training-heart-rates
    # https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

    result = entity.StatusEnum.LIFE_THREATENING
    options = {
        entity.StatusEnum.OK: (60, 100),
        entity.StatusEnum.MINOR: (50, 120),
        entity.StatusEnum.MAJOR: (40, 160),
    }

    for status in options:
        min, max = options[status]
        if min <= pulse <= max:
            result = status
            break
    return result


def pulse_analysis(
    pulse: int, measurement_statistics: entity.MeasurementStatistics
) -> entity.StatusEnum:
    """
    Analysis pulse and deremines status of it and updates statistics for that
    status.

    :param: pulse Pulse to analyse.
    :param: measurement_statistics Statistics to update.
    :return: Analysed pulse status.
    :raises: TypeError When an non numeric pulse was given.
    """
    result = entity.StatusEnum.MISSING
    if not str(pulse).isnumeric():
        raise TypeError("Pulse should be a whole positive number")

    if str(pulse).isnumeric() and 0 < pulse < 230:
        result = _pulse_analysis_determine(pulse)

    measurement_statistics.increment(result)
    return result


def blood_pressure_systolic_analysis(
    blood_pressure_systolic: int, measurement_statistics: entity.MeasurementStatistics
) -> entity.StatusEnum:
    """
    Checks validation and valuation and increment status in statistics of
    systolic pressure..

    :param: blood_pressure_systolic The systolic blood pressure level to analyse.
    :param: measurement_statistics The statistics to update with the analysis.
    :return The result of the analysis.
    """

    if not blood_pressure_systolic_validation(blood_pressure_systolic):
        measurement_statistics.increment(entity.StatusEnum.MISSING)
        return entity.StatusEnum.MISSING

    status = blood_pressure_systolic_valuation(blood_pressure_systolic)
    measurement_statistics.increment(status)
    return status


def blood_pressure_systolic_validation(blood_pressure_systolic: int) -> bool:
    """
    Checks if it is an integer and if the number is between -1 and 251.

    :param: blood_pressure_systolic: The blood pressure to check.
    :return True if a valid value was given.
    """

    if not str(blood_pressure_systolic).isnumeric():
        return False

    return int(blood_pressure_systolic) < 251 and int(blood_pressure_systolic) >= 0


def blood_pressure_systolic_valuation(
    blood_pressure_systolic: int,
) -> entity.StatusEnum:
    """
    Checks different values to assign a status to.

    :param: blood_pressure_systolic systolic blood pressure level to evaluate.
    :return Status of the systolic blood pressure.
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
    else:
        return entity.StatusEnum.OK


def blood_pressure_diastolic_analysis(
    blood_pressure_diastolic: int, measurement_statistics: entity.MeasurementStatistics
) -> entity.StatusEnum:
    """
    Checks validation and valuation and increment status in statistics of
    diastolic pressure..

    :param: blood_pressure_diastolic The diastolic blood pressure level to analyse.
    :param: measurement_statistics The statistics to update with the analysis.
    :return The result of the analysis.
    """

    if not blood_pressure_diastolic_validation(blood_pressure_diastolic):
        measurement_statistics.increment(entity.StatusEnum.MISSING)
        return entity.StatusEnum.MISSING

    status = blood_pressure_diastolic_valuation(blood_pressure_diastolic)
    measurement_statistics.increment(status)
    return status


def blood_pressure_diastolic_validation(blood_pressure_diastolic: int) -> bool:
    """
    Checks if it is an integer and if the number is between -1 and 141.

    :param: blood_pressure_diastolic: The blood pressure to check.
    :return True if a valid value was given.
    """

    if not str(blood_pressure_diastolic).isnumeric():
        return False

    return int(blood_pressure_diastolic) < 141 and int(blood_pressure_diastolic) >= 0


def blood_pressure_diastolic_valuation(
    blood_pressure_diastolic: int,
) -> entity.StatusEnum:
    """
    Checks different values to assign a status to.

    :param: blood_pressure_diastolic Blood pressure level to evaluate.
    :return Status of the diastolic blood pressure.
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
    else:
        return entity.StatusEnum.OK
