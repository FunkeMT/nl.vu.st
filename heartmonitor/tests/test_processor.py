"""Tests for `heartmonitor` package."""
import pytest
import processor, entity
from numbers import Number

m1 = entity.Measurement(90,50,30,40)
m2 = entity.Measurement(22,88,44,66)
m3 = entity.Measurement(36,0,1,44)
m4 = entity.Measurement(234,36,453,24)
mock = entity.MockRecording([m1,m2,m3,m4])

def test_oxygen_validation1(capsys):
    assert not processor.oxygen_validation(-1)


def test_oxygen_validation2(capsys):
    assert not processor.oxygen_validation(-44)


def test_oxygen_validation3(capsys):
    assert not processor.oxygen_validation(101)


def test_oxygen_validation4(capsys):
    assert not processor.oxygen_validation(133)


def test_oxygen_validation5(capsys):
    assert not processor.oxygen_validation("133")


def test_oxygen_validation6(capsys):
    assert isinstance(m1.oxygen, Number)
    assert m1.oxygen <= 100 and m1.oxygen >= 0


def test_oxygen_validation7(capsys):
    assert not processor.oxygen_validation("asd")


def test_oxygen_analysis1(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0

    assert entity.StatusEnum.MISSING == processor.oxygen_analysis(-1, stats)

    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 1


def test_oxygen_analysis2(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0

    assert entity.StatusEnum.MISSING == processor.oxygen_analysis(-44, stats)

    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 1


def test_oxygen_analysis3(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0

    assert entity.StatusEnum.MISSING == processor.oxygen_analysis(101, stats)

    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 1


def test_oxygen_analysis4(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0

    assert entity.StatusEnum.MISSING == processor.oxygen_analysis(133, stats)

    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 1


def test_oxygen_analysis5(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0

    assert entity.StatusEnum.MISSING == processor.oxygen_analysis("133", stats)

    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 1


def test_oxygen_analysis6(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0

    assert entity.StatusEnum.MISSING == processor.oxygen_analysis("asd", stats)

    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 1


def test_oxygen_analysis7(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0
    
    assert processor.oxygen_analysis(95, stats) == entity.StatusEnum.OK

    assert stats.missing_count == 0
    assert stats.ok_count == 1
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0


def test_oxygen_analysis8(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0
    
    assert processor.oxygen_analysis(90, stats) == entity.StatusEnum.MINOR

    assert stats.missing_count == 0
    assert stats.ok_count == 0
    assert stats.minor_count == 1
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0


def test_oxygen_analysis9(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0
    
    assert processor.oxygen_analysis(61, stats) == entity.StatusEnum.MAJOR

    assert stats.missing_count == 0
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 1
    assert stats.life_threatening_count == 0


def test_oxygen_analysis10(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0
    
    assert processor.oxygen_analysis(6, stats) == entity.StatusEnum.LIFE_THREATENING

    assert stats.missing_count == 0
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 1


def test_oxygen_analysis11(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0
    
    assert processor.oxygen_analysis(-1, stats) == entity.StatusEnum.MISSING

    assert stats.missing_count == 1
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0


def test_oxygen_analysis12(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0
    
    assert processor.oxygen_analysis(101, stats) == entity.StatusEnum.MISSING

    assert stats.missing_count == 1
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0


def test_oxygen_analysis13(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0
    
    assert processor.oxygen_analysis(0, stats) == entity.StatusEnum.LIFE_THREATENING

    assert stats.missing_count == 0
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 1


def test_oxygen_analysis14(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0
    
    assert processor.oxygen_analysis(60, stats) == entity.StatusEnum.LIFE_THREATENING

    assert stats.missing_count == 0
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 1


def test_oxygen_analysis15(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0
    
    assert processor.oxygen_analysis(61, stats) == entity.StatusEnum.MAJOR

    assert stats.missing_count == 0
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 1
    assert stats.life_threatening_count == 0


def test_oxygen_analysis16(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0
    
    assert processor.oxygen_analysis(89, stats) == entity.StatusEnum.MAJOR

    assert stats.missing_count == 0
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 1
    assert stats.life_threatening_count == 0


def test_oxygen_analysis17(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0
    
    assert processor.oxygen_analysis(90, stats) == entity.StatusEnum.MINOR

    assert stats.missing_count == 0
    assert stats.ok_count == 0
    assert stats.minor_count == 1
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0


def test_oxygen_analysis18(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0
    
    assert processor.oxygen_analysis(94, stats) == entity.StatusEnum.MINOR

    assert stats.missing_count == 0
    assert stats.ok_count == 0
    assert stats.minor_count == 1
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0


def test_oxygen_analysis19(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0
    
    assert processor.oxygen_analysis(95, stats) == entity.StatusEnum.OK

    assert stats.missing_count == 0
    assert stats.ok_count == 1
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0


def test_oxygen_analysis20(capsys):
    """Testing oxygen_analysis"""
    stats = entity.MeasurementStatistics()
    assert stats.ok_count == 0
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0
    assert stats.missing_count == 0
    
    assert processor.oxygen_analysis(100, stats) == entity.StatusEnum.OK

    assert stats.missing_count == 0
    assert stats.ok_count == 1
    assert stats.minor_count == 0
    assert stats.major_count == 0
    assert stats.life_threatening_count == 0


def test_pulse_analysis_determine1(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(1) == entity.StatusEnum.LIFE_THREATENING


def test_pulse_analysis_determine2(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(-1) == entity.StatusEnum.LIFE_THREATENING


def test_pulse_analysis_determine3(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(0) == entity.StatusEnum.LIFE_THREATENING


def test_pulse_analysis_determine4(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(40) == entity.StatusEnum.MAJOR


def test_pulse_analysis_determine5(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(50) == entity.StatusEnum.MINOR


def test_pulse_analysis_determine6(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(60) == entity.StatusEnum.OK


def test_pulse_analysis_determine7(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(90) == entity.StatusEnum.OK


def test_pulse_analysis_determine8(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(100) == entity.StatusEnum.OK


def test_pulse_analysis_determine9(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(120) == entity.StatusEnum.MINOR


def test_pulse_analysis_determine10(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(160) == entity.StatusEnum.MAJOR


def test_pulse_analysis_determine11(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(101) == entity.StatusEnum.MINOR


def test_pulse_analysis_determine12(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(121) == entity.StatusEnum.MAJOR


def test_pulse_analysis_determine13(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(161) == entity.StatusEnum.LIFE_THREATENING


def test_pulse_analysis_determine14(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(39) == entity.StatusEnum.LIFE_THREATENING


def test_pulse_analysis_determine15(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(49) == entity.StatusEnum.MAJOR


def test_pulse_analysis_determine16(capsys):
    """Testing test_pulse_analysis_determine"""
    assert processor._pulse_analysis_determine(59) == entity.StatusEnum.MINOR


def test_pulse_analysis1(capsys):
    """Testing pulse_analysis"""
    happend = False
    try:
        processor.pulse_analysis("a", None)
    except TypeError:
        happend = True

    assert happend


def test_pulse_analysis2(capsys):
    """Testing pulse_analysis"""
    happend = False
    try:
        processor.pulse_analysis("9", None)
    except TypeError:
        happend = True

    assert happend

def test_pulse_analysis11(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(1, stats)
    assert stats.life_threatening_count == 1
    assert res == entity.StatusEnum.LIFE_THREATENING


def test_pulse_analysis12(capsys):
    """Testing test_pulse_analysis_determine"""
    happend = False
    try:
        stats = entity.MeasurementStatistics()
        processor.pulse_analysis(-1, stats)
    except TypeError: 
        happend = True
    assert happend


def test_pulse_analysis13(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(0, stats)
    assert stats.missing_count == 1
    assert res == entity.StatusEnum.MISSING


def test_pulse_analysis14(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(40, stats)
    assert stats.major_count == 1
    assert res == entity.StatusEnum.MAJOR


def test_pulse_analysis15(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(50, stats)
    assert stats.minor_count == 1
    assert res == entity.StatusEnum.MINOR


def test_pulse_analysis16(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(60, stats)
    assert stats.ok_count == 1
    assert res == entity.StatusEnum.OK


def test_pulse_analysis17(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(90, stats)
    assert stats.ok_count == 1
    assert res == entity.StatusEnum.OK


def test_pulse_analysis18(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(100, stats)
    assert stats.ok_count == 1
    assert res == entity.StatusEnum.OK


def test_pulse_analysis19(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(120, stats)
    assert stats.minor_count == 1
    assert res == entity.StatusEnum.MINOR


def test_pulse_analysis110(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(160, stats)
    assert stats.major_count == 1
    assert res == entity.StatusEnum.MAJOR


def test_pulse_analysis111(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(101, stats)
    assert stats.minor_count == 1
    assert res == entity.StatusEnum.MINOR


def test_pulse_analysis112(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(121, stats)
    assert stats.major_count == 1
    assert res == entity.StatusEnum.MAJOR


def test_pulse_analysis113(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(161, stats)
    assert stats.life_threatening_count == 1
    assert res == entity.StatusEnum.LIFE_THREATENING


def test_pulse_analysis114(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(39, stats)
    assert stats.life_threatening_count == 1
    assert res == entity.StatusEnum.LIFE_THREATENING


def test_pulse_analysis115(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(49, stats)
    assert stats.major_count == 1
    assert res == entity.StatusEnum.MAJOR


def test_pulse_analysis116(capsys):
    """Testing test_pulse_analysis_determine"""
    stats = entity.MeasurementStatistics()
    res = processor.pulse_analysis(59, stats)
    assert stats.minor_count == 1
    assert res == entity.StatusEnum.MINOR


def test_pulse_analysis3(capsys):
    """Testing pulse_analysis"""
    happend = False
    try:
        processor.pulse_analysis("99.9", None)
    except TypeError:
        happend = True

    assert happend


def test_oxygen_measure(capsys):
    assert processor.oxygen_valuation(95) == entity.StatusEnum.OK
    assert processor.oxygen_valuation(90) == entity.StatusEnum.MINOR
    assert processor.oxygen_valuation(61) == entity.StatusEnum.MAJOR
    assert processor.oxygen_valuation(6) == entity.StatusEnum.LIFE_THREATENING
