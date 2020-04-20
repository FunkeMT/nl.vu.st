"""Tests for `heartmonitor` package."""
import pytest
from heartmonitor import argv_parser


def test_argv_parse_1(capsys):
    """Correct name argument and printing"""
    res = argv_parser.parse(["--test", "hello"], "--test")
    assert "hello" == res


def test_argv_parse_2(capsys):
    """Correct name argument and printing"""
    happend = False
    try:
        argv_parser.parse(["--test", "hello"], "--test2")
    except NameError:
        happend = True
    assert happend

def test_argv_parse_3(capsys):
    """Correct name argument and printing"""
    happend = False
    try:
        argv_parser.parse([], "--test2")
    except NameError:
        happend = True
    assert happend

def test_argv_parse_4(capsys):
    """Correct name argument and printing"""
    happend = False
    try:
        argv_parser.parse([], "")
    except NameError:
        happend = True
    assert happend

def test_argv_parse_5(capsys):
    """Correct name argument and printing"""
    res = argv_parser.parse(["--test"], "--test")
    assert True == res
