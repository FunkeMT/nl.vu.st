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
	happend = False
	try:
		processor.oxygen_validity_checker(-1)
	except Exception:
		happend = True
	assert happend

def test_oxygen_validity_checker2(capsys):
	happend = False
	try:
		processor.oxygen_validity_checker(-44)
	except Exception:
		happend = True
	assert happend

def test_oxygen_validity_checker3(capsys):
	happend = False
	try:
		processor.oxygen_validity_checker(101)
	except Exception:
		happend = True
	assert happend

def test_oxygen_validity_checker4(capsys):
	happend = False
	try:
		processor.oxygen_validity_checker(133)
	except Exception:
		happend = True
	assert happend

def test_oxygen_validity_checker5(capsys):
	happend = False
	try:
		processor.oxygen_validity_checker("133")
	except Exception:
		happend = True
	assert happend

def test_oxygen_validity_checker5(capsys):
    assert isinstance(m1.oxygen, Number)
    assert m1.oxygen <= 100 and m1.oxygen >= 0

