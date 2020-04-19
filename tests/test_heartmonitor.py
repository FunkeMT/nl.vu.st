"""Tests for `heartmonitor` package."""
import pytest
from heartmonitor import heartmonitor


def test_convert(capsys):
    """Correct name argument and printing"""
    notebookc.convert("World")
    captured = capsys.readouterr()
    assert "World" in captured.out
