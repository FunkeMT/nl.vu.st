from datetime import datetime
import os
import entity


def format_statistics(s: entity.Statistics) -> str:
    """
    Formats the statistics with color for status
    
    :param: s: statistics object
    :return: string object of the printed statistics
    """

    pulsestring = "Pulse statistics:                    "
    pulsecontent = format_measurement_statistics(s.pulse)
    oxygenstring = "Oxygen statistics:                   "
    oxygencontent = format_measurement_statistics(s.oxygen)
    systolicstring = "Blood pressure systolic statistics:  "
    systoliccontent = format_measurement_statistics(s.blood_pressure_systolic)
    diastolicstring = "Blood pressure diastolic statistics: "
    diastoliccontent = format_measurement_statistics(s.blood_pressure_diastolic)
    finishedstring = "Simulation Finished"

    return (
        pulsestring
        + pulsecontent
        + os.linesep
        + oxygenstring
        + oxygencontent
        + os.linesep
        + systolicstring
        + systoliccontent
        + os.linesep
        + diastolicstring
        + diastoliccontent
        + os.linesep
        + finishedstring
    )


def format_measurement_statistics(ms: entity.MeasurementStatistics) -> str:
    """
    formats a MeasuremenStatistics object with color for status
    
    :param: ms: MeasurementStatistics object
    :return: string object of the printed values
    """
    statisticsstring = "[OK: {ok:3}; MISSING: {missing:3}; MINOR: {minor:3}; MAJOR: {major:3}; LIFE_THREATENING: {lt:3}]".format(
        ok=ms.ok_count,
        missing=ms.missing_count,
        minor=ms.minor_count,
        major=ms.major_count,
        lt=ms.life_threatening_count,
    )

    return statisticsstring


def format_status(mr: entity.MeasurementResult) -> str:
    """
    Formats measurement results

    "param" mr: MeasurementResult object
    "return" the string that is printed to the screen
    """

    now = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    datestring = "[{time}]".format(time=now)
    pulsestring = "Pulse: {pulse:3} bpm, status: {pulse_status:17}".format(
        pulse=mr.m.pulse, pulse_status=mr.pulse_status.value
    )
    oxygenstring = "SaO2: {oxygen:2}% status: {oxygen_status:17}".format(
        oxygen=mr.m.oxygen, oxygen_status=mr.oxygen_status.value
    )
    bloodpressurestring = "Blood pressure: {systolic:3}/{diastolic:3} mm Hg, Systolic status: {systolic_status:17}| Diastolic status: {diastolic_status:17}".format(
        systolic=mr.m.blood_pressure_systolic,
        diastolic=mr.m.blood_pressure_diastolic,
        systolic_status=mr.blood_pressure_systolic_status.value,
        diastolic_status=mr.blood_pressure_diastolic_status.value,
    )

    return (
        datestring
        + " | "
        + pulsestring
        + "| "
        + oxygenstring
        + "| "
        + bloodpressurestring
    )
