from enum import Enum
from typing import List


class StatusEnum(Enum):
    """
    Status of a measurement.
    """
    OK = "OK"
    MISSING = "MISSING"
    MINOR = "MINOR"
    MAJOR = "MAJOR"
    LIFE_THREATENING = "LIFE_THREATENING"

class GenderEnum(Enum):
    """
    Gender of a patient.
    """
    MALE = "MALE"
    FEMALE = "FEMALE"

class Patient:
    def __init__(self, age: int, height: int, weight: int, gender: GenderEnum):
        """
        Patient information.
        """
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        
class Measurement:
    def __init__(self, oxygen: int = None, pulse: int = None,
        blood_pressure_systolic: int = None,
        blood_pressure_diastolic: int = None):
        """
        Snap shot of measurement information. 
        """
        self.oxygen = oxygen
        self.pulse = pulse
        self.blood_pressure_systolic = blood_pressure_systolic
        self.blood_pressure_diastolic = blood_pressure_diastolic
    
class AbstractRecording:
    """
    Abstract recording.
    """
    def get_iterator(self): return iter(self)
    def __iter__(self): return self
    def __next__(self): raise StopIteration

class FileRecording(AbstractRecording):
    def __init__(self, filepath: str):
        """
        File recording, that can be used for loop through a recording.
        """
        self.filepath = filepath
        # @todo implement this class
        raise NotImplementedError

class MockRecording(AbstractRecording):
    def __init__(self, results: List[Measurement]):
        """"
        Recording that can be used for testing.
        """"
        self.results = results
    
    def get_iterator(self): return iter(self.results)
    def __iter__(self): return self.results

class MeasurementStatistics:
    def __init__(self, ok_count: int = 0, missing_count: int = 0, 
        minor_count: int = 0, major_count: int = 0, 
        life_threatening_count: int = 0):
        """
        Measurement statistics of a single sensor.
        """
        self.ok_count = ok_count
        self.missing_count = missing_count
        self.minor_count = minor_count
        self.major_count = major_count
        self.life_threatening_count = life_threatening_count

    def increment(self, status: StatusEnum):
        """
        Increment a measurement status.
        """
        if status == StatusEnum.OK:
            self.ok_count += 1
        elif status == StatusEnum.MISSING:
            self.missing_count += 1
        elif status == StatusEnum.MINOR:
            self.minor_count += 1
        elif status == StatusEnum.MAJOR:
            self.major_count += 1
        elif status == StatusEnum.LIFE_THREATENING:
            self.life_threatening_count += 1

class Statistics:
    def __init__(self, oxygen: MeasurementStatistics, 
        pulse: MeasurementStatistics, bloodpressure: MeasurementStatistics):
        """
        Statistics of different sensors.
        """
        self.oxygen = oxygen
        self.pulse = pulse
        self.bloodpressure = bloodpressure

