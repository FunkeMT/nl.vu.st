import entity

def ps(measurement: entity.Measurement):
    oxygen_status = process_oxygen(measurement.oxygen)
    #pulse_status = process_pulse(pulse)
    #systolic_status = process_bp_systolic(bp_systolic)
    #diastolic_status = process_bp_diastolic(bp_diastolic)
    return {"oxygen": oxygen_status} # add the last statusses when implemented

def process_oxygen(oxygen):
    if not oxygen_validity_checker(oxygen):
        return entity.StatusEnum.MISSING.value
    return oxygen_measure(oxygen).value

def oxygen_validity_checker(oxygen: int):
    if not str(oxygen).isnumeric():
    	return False

    if (int(oxygen) < 101 and int(oxygen) >= 0): 
        return True
    else:
        return False

def oxygen_measure(oxygen):
    if oxygen >= 95: return entity.StatusEnum.OK
    elif oxygen >= 90: return entity.StatusEnum.MINOR
    elif oxygen > 60: return entity.StatusEnum.MAJOR
    elif oxygen <= 60: return entity.StatusEnum.LIFE_THREATENING

def process_pulse(pulse):
	# To be implemented
    pass

def process_bp_systolic(bp_systolic):
	# To be implemented
    pass

def process_bp_diastolic(bp_diastolic):
	# To be implemented
    pass