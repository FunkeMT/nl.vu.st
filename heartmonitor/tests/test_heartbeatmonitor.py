"""Tests for `heartmonitor.entity` package."""
import pytest
import heartbeatmonitor


def test_help(capsys):
    """Correct name argument and printing"""
    heartbeatmonitor.print_help()
    captured = capsys.readouterr()
    lines = captured.out.split("\n")
    assert "Command usage is as follows:" == lines[0]
    assert "heartbeatmonitor.py arguments:" == lines[1]
    assert "" == lines[2]
    assert "Arguments are the following:" == lines[3]
