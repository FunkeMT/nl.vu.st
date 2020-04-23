"""Tests for `heartmonitor` package."""
import pytest
import entity
from numbers import Number

def test_oxygen_validity_checker(capsys):
    m = entity.Measurement()
    assert isinstance(m.oxygen, Number)
    assert m.oxygen <= 100 or m.oxygen >= 0
