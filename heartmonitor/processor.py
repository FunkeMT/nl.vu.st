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

    #pulse_status = process_pulse(pulse)
    #systolic_status = process_blood_pressure_systolic(blood_pressure_systolic)
    #diastolic_status = process_blood_pressure_diastolic(blood_pressure_diastolic)

    # Add new statuses to the result
    measurement_results = entity.MeasurementResult(measurement, oxygen_status)

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
    if oxygen >= 95: return entity.StatusEnum.OK
    elif oxygen >= 90: return entity.StatusEnum.MINOR
    elif oxygen > 60: return entity.StatusEnum.MAJOR
    elif oxygen <= 60: return entity.StatusEnum.LIFE_THREATENING

def process_pulse(pulse):
	# To be implemented
    pass

def process_blood_pressure_systolic(blood_pressure_systolic):
	# To be implemented
    pass

def process_blood_pressure_diastolic(blood_pressure_diastolic):
	# To be implemented
    pass