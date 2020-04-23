import entity

def processor(oxygen, pulse, blood_pressure):
    process_oxygen(oxygen)
    process_pulse(pulse)
    process_blood_pressure(blood_pressure)


def process_oxygen(oxygen):
    if not oxygen_validity_checker(oxygen):
        entity.MeasurementStatistics().increment(entity.StatusEnum.MISSING)
        return entity.StatusEnum.MISSING.value
    
    entity.MeasurementStatistics().increment(oxygen_measure())
    print(oxygen_measure().value)
    return oxygen_measure().value

def oxygen_validity_checker(oxygen):
    if str(oxygen).isnumeric() and (oxygen < 101 and oxygen >= 0): 
        return True
    else:
        return False

def oxygen_measure():
    if entity.Measurement.oxygen >= 95: return entity.StatusEnum.OK
    elif entity.Measurement.oxygen >= 90: return entity.StatusEnum.MINOR
    elif entity.Measurement.oxygen > 60: return entity.StatusEnum.MAJOR
    elif entity.Measurement.oxygen <= 60: return entity.StatusEnum.LIFE_THREATENING

def process_pulse(pulse):
    pass

def process_blood_pressure(blood_pressure):
    pass