"""Tests for `heartmonitor.entity` package."""
import pytest
import heartbeatmonitor
import datetime

def test_help(capsys):
    """Correct name argument and printing"""
    heartbeatmonitor.print_help()
    captured = capsys.readouterr()
    lines = captured.out.split("\n")
    assert "Command usage is as follows:" == lines[0]
    assert "heartbeatmonitor.py arguments:" == lines[1]
    assert "" == lines[2]
    assert "Arguments are the following:" == lines[3]


def test_MEASUREMENT_INTERVAL_IN_MS(capsys):
    """Testing MEASUREMENT_INTERVAL_IN_MS"""
    assert heartbeatmonitor.MEASUREMENT_INTERVAL_IN_MS == 500


def test_MILLISECONDS_IN_SECOND(capsys):
    """Testing MILLISECONDS_IN_SECOND"""
    assert heartbeatmonitor.MILLISECONDS_IN_SECOND == 1000


def test_wait_on_new_measurement(capsys):
    """Testing wait_on_new_measurement"""
    before_timestamp = datetime.datetime.now().timestamp()
    assert heartbeatmonitor.wait_on_new_measurement() is None
    difference = (datetime.datetime.now().timestamp() - before_timestamp) * 1000
    assert difference - 1 <= heartbeatmonitor.MEASUREMENT_INTERVAL_IN_MS
    assert difference + 1 >= heartbeatmonitor.MEASUREMENT_INTERVAL_IN_MS
