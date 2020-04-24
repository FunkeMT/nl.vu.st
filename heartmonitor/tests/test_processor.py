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

def test_oxygen_measure(capsys):
    assert processor.oxygen_valuation(95) == entity.StatusEnum.OK
    assert processor.oxygen_valuation(90) == entity.StatusEnum.MINOR
    assert processor.oxygen_valuation(61) == entity.StatusEnum.MAJOR
    assert processor.oxygen_valuation(6) == entity.StatusEnum.LIFE_THREATENING
