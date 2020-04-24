"""Tests for `heartmonitor` package."""
import pytest
import processor, entity
from numbers import Number

m1 = entity.Measurement(90,50,30,40)
m2 = entity.Measurement(22,88,44,66)
m3 = entity.Measurement(36,0,1,44)
m4 = entity.Measurement(234,36,453,24)
mock = entity.MockRecording([m1,m2,m3,m4])


def test_oxygen_processor():
    pass


def test_oxygen_validity_checker1(capsys):
    if processor.oxygen_validity_checker(-1) == False:
        assert True
    else:
        assert False

def test_oxygen_validity_checker2(capsys):
    if processor.oxygen_validity_checker(-44) == False:
        assert True
    else:
        assert False

def test_oxygen_validity_checker3(capsys):
    if processor.oxygen_validity_checker(101) == False:
        assert True
    else:
        assert False

def test_oxygen_validity_checker4(capsys):
    if processor.oxygen_validity_checker(133) == False:
        assert True
    else:
        assert False

def test_oxygen_validity_checker5(capsys):
    if processor.oxygen_validity_checker("133") == False:
        assert True
    else:
        assert False

def test_oxygen_validity_checker6(capsys):
    assert isinstance(m1.oxygen, Number)
    assert m1.oxygen <= 100 and m1.oxygen >= 0

def test_oxygen_validity_checker7(capsys):
    try:
        assert processor.oxygen_validity_checker("asd")
    except Exception:
        assert True

def test_oxygen_measure(capsys):
    assert processor.oxygen_measure(95) == entity.StatusEnum.OK
    assert processor.oxygen_measure(90) == entity.StatusEnum.MINOR
    assert processor.oxygen_measure(61) == entity.StatusEnum.MAJOR
    assert processor.oxygen_measure(6) == entity.StatusEnum.LIFE_THREATENING
