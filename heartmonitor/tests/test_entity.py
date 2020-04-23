"""Tests for `heartmonitor.entity` package."""
import pytest
import entity


def test_StatusEnum(capsys):
    """Testing entity StatusEnum"""
    data = entity.StatusEnum.__dict__
    keys = []
    for k in data:
        if k.startswith("_"): continue
        keys.append(k)

    assert "OK" in keys
    assert "MISSING" in keys
    assert "MINOR" in keys
    assert "MAJOR" in keys
    assert "LIFE_THREATENING" in keys
    assert 5 == len(keys)


def test_GenderEnum(capsys):
    """Testing entity GenderEnum"""
    data = entity.GenderEnum.__dict__
    keys = []
    for k in data:
        if k.startswith("_"): continue
        keys.append(k)

    assert "MALE" in keys
    assert "FEMALE" in keys
    assert 2 == len(keys)


def test_Patient(capsys):
    """Testing entity Patient"""
    patient = entity.Patient(25, 180, 75, entity.GenderEnum.MALE)

    assert patient.age == 25
    assert patient.height == 180
    assert patient.weight == 75
    assert patient.gender == entity.GenderEnum.MALE


def test_Measurement(capsys):
    """Testing entity Measurement"""
    m = entity.Measurement()

    assert m.oxygen is None
    assert m.pulse is None
    assert m.blood_pressure_systolic is None
    assert m.blood_pressure_diastolic is None


def test_MeasurementValues(capsys):
    """Testing entity MeasurementValues"""
    m = entity.Measurement(10, 20, 30, 40)

    assert m.oxygen == 10
    assert m.pulse == 20
    assert m.blood_pressure_systolic == 30
    assert m.blood_pressure_diastolic == 40


def test_AbstractRecording(capsys):
    """Testing entity AbstractRecording"""
    ar = entity.AbstractRecording()

    assert isinstance(ar.get_iterator(), entity.AbstractRecording)

    happend = False
    try:
        ar.__next__()
    except StopIteration:
        happend = True
    assert happend

    assert ar == ar.__iter__()


def test_FileRecording(capsys):
    """Testing entity FileRecording"""
    happend = False
    try:
        fr = entity.FileRecording("path")
    except NotImplementedError:
        happend = True
    assert happend


def test_MockRecording(capsys):
    """Testing entity MockRecording"""
    mr = entity.MockRecording([entity.Measurement(10)])

    assert len(mr.results) == 1
    assert mr.results[0].oxygen == 10
    assert mr.results[0].pulse is None

    for x in mr.get_iterator():
        assert mr.results[0] == x


def test_MeasurementStatistics(capsys):
    """Testing entity MeasurementStatistics"""
    ms = entity.MeasurementStatistics()

    assert ms.ok_count == 0
    assert ms.missing_count == 0
    assert ms.minor_count == 0
    assert ms.major_count == 0
    assert ms.life_threatening_count == 0


def test_MeasurementStatistics(capsys):
    """Testing entity MeasurementStatistics"""
    ms = entity.MeasurementStatistics(0, 1, 2, 3, 4)
    
    data = entity.StatusEnum.__dict__
    for k in data:
        if k.startswith("_"): continue
        prev_value = ms.__getattribute__(k.lower() + "_count")
        ms.increment(data[k])
        assert prev_value == ms.__getattribute__(k.lower() + "_count") - 1


def test_Statistics(capsys):
    """Testing entity Statistics"""
    oxygen = entity.MeasurementStatistics()
    pulse = entity.MeasurementStatistics()
    bloodpressure = entity.MeasurementStatistics()

    s = entity.Statistics(oxygen, pulse, bloodpressure) 
    assert s.oxygen == oxygen
    assert s.pulse == pulse
    assert s.bloodpressure == bloodpressure
