"""Tests for `heartmonitor` package."""
import pytest
from heartmonitor import heartmonitor


def test_convert(capsys):
    """Correct name argument and printing"""
    heartmonitor.hello("World")
    captured = capsys.readouterr()
    assert "World" in captured.out
