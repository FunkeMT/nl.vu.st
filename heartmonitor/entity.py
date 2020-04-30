from enum import Enum
from typing import List
import os
import csv


class StatusEnum(Enum):
    """
    Status of a measurement.
    """

    OK = "OK"
    MISSING = "MISSING"
    MINOR = "MINOR"
    MAJOR = "MAJOR"
    LIFE_THREATENING = "LIFE_THREATENING"


class Measurement:
    def __init__(
        self,
        oxygen: int = None,
        pulse: int = None,
        blood_pressure_systolic: int = None,
        blood_pressure_diastolic: int = None,
    ):
        """
        Snap shot of measurement information. 
        """
        self.oxygen = oxygen
        self.pulse = pulse
        self.blood_pressure_systolic = blood_pressure_systolic
        self.blood_pressure_diastolic = blood_pressure_diastolic


class MeasurementResult:
    def __init__(
        self,
        m: Measurement,
        oxygen_status: StatusEnum = StatusEnum.MISSING,
        pulse_status: StatusEnum = StatusEnum.MISSING,
        blood_pressure_systolic_status: StatusEnum = StatusEnum.MISSING,
        blood_pressure_diastolic_status: StatusEnum = StatusEnum.MISSING,
    ):
        """
        Object that holds results of processing as well as original measurement

        """

        self.oxygen_status = oxygen_status
        self.pulse_status = pulse_status
        self.blood_pressure_systolic_status = blood_pressure_systolic_status
        self.blood_pressure_diastolic_status = blood_pressure_diastolic_status
        self.m = m


class AbstractRecording:
    """
    Abstract recording.
    """

    def get_iterator(self):
        return iter(self)

    def __iter__(self):
        return self

    def __next__(self, make_invalid_measurement_missing: bool=False) -> Measurement:  # pragma: no mutate
        raise StopIteration


class FileNotFound(Exception): pass


class FileRecording(AbstractRecording):
    def __init__(self, filepath: str):
        """
        File recording, that can be used for loop through a recording.

        :param: filepath: File path to the recording.
        :raises: AssertionError When a header field was missing.
        :raises: Exception When the file could not be found.
        """
        self._fpointer = None  # pragma: no mutate
        self.filepath = filepath
        if not os.path.exists(filepath):
            raise FileNotFound("Could not find recording file.")

        self._fpointer = open(self.filepath, "r")
        parts = next(csv.reader([self._fpointer.readline()]))
        self._validate_heading(parts)

        (
            self.index_oxygen,
            self.index_pulse,
            self.index_systolic,
            self.index_diastolic,
        ) = self._get_indices(
            parts,
            ["oxygen", "pulse", "blood_pressure_systolic", "blood_pressure_diastolic"],
        )

    def _get_indices(self, parts: List[str], keys: List[str]):
        """
        Get the index of each given field in the parts given.

        :param: parts Parts to search in.
        :param: keys Keys to search for.
        :return: Yields in order the index for each key that was given.
        """
        for key in keys:
            yield parts.index(key)

    def _validate_heading(self, heading_parts: List[str]):
        """
        Validates the given header row.

        :raises: AssertionError When a field was missing.
        """
        # Validate heading row.
        assert len(heading_parts) >= 4
        assert "oxygen" in heading_parts
        assert "pulse" in heading_parts
        assert "blood_pressure_systolic" in heading_parts
        assert "blood_pressure_diastolic" in heading_parts


    def _parse_field(self, line: List[str], index: int,
        make_invalid_measurement_missing: bool=False) -> int:
        """
        Parse a CSV field into an int value.

        :param: line Parsed CSV line.
        :param: index Index of the value.
        :param: make_invalid_measurement_missing Make invalid values None.
        :return: Value of the field parsed into a int value.
        :raises: ValueError When make_invalid_measurement_missing was not
                            set and an incorrect value was parsed.
        """
        result = None
        try:
            if line[index]:
                result = int(line[index])
        except ValueError as ex:
            if not make_invalid_measurement_missing: raise ex
            result = None
        return result


    def _line_to_measurement(self, line: List[str], 
        make_invalid_measurement_missing: bool=False) -> Measurement:
        """
        Convert a parsed CSV line to a measurement object.

        :param: line Parsed CSV line.
        :param: make_invalid_measurement_missing Make invalid values None.
        :return: Line that has been parsed to a measurement object. 
        :raises: ValueError When make_invalid_measurement_missing was not
                            set and an incorrect value was parsed.
        """
        res = Measurement()
        res.oxygen = self._parse_field(line, self.index_oxygen,
            make_invalid_measurement_missing)
        res.pulse = self._parse_field(line, self.index_pulse,
            make_invalid_measurement_missing)
        res.blood_pressure_systolic = self._parse_field(line,
            self.index_systolic, make_invalid_measurement_missing)
        res.blood_pressure_diastolic = self._parse_field(line,
            self.index_diastolic, make_invalid_measurement_missing)

        return res

    def __next__(self, make_invalid_measurement_missing: bool=False) -> Measurement:  # pragma: no mutate
        """
        Read the next measurement from file.

        :param: make_invalid_measurement_missing Make invalid values None.
        :return The measurement that has been read from disk.
        :raises: ValueError When an measurement doesnot contain integer values.
        :raises: IndexError When a field is missing in a recording line.
        """
        try:
            line = self._fpointer.readline()
            parts = next(csv.reader([line]))
            if not parts:
                raise StopIteration
            return self._line_to_measurement(parts, make_invalid_measurement_missing)
        except StopIteration:
            raise StopIteration

    def __del__(self):
        """
        When we destroy our recording object we need to close the file handler, 
        to free up resources.

        :raises: Exception: When there was an error releasing the file handler.
        """
        if self._fpointer is not None and not self._fpointer.closed:  # pragma: no mutate
            self._fpointer.close()


class MockRecording(AbstractRecording):
    def __init__(self, results: List[Measurement]):
        """
        Recording that can be used for testing.
        """
        self.results = results

    def get_iterator(self):
        return iter(self.results)

    def __iter__(self):
        return self.results


class MeasurementStatistics:
    def __init__(
        self,
        ok_count: int = 0,
        missing_count: int = 0,
        minor_count: int = 0,
        major_count: int = 0,
        life_threatening_count: int = 0,
    ):
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
    def __init__(
        self,
        oxygen: MeasurementStatistics,
        pulse: MeasurementStatistics,
        blood_pressure_systolic: MeasurementStatistics,
        blood_pressure_diastolic: MeasurementStatistics,
    ):
        """
        Statistics of different sensors.
        """
        self.oxygen = oxygen
        self.pulse = pulse
        self.blood_pressure_systolic = blood_pressure_systolic
        self.blood_pressure_diastolic = blood_pressure_diastolic
