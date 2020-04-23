"""Tests for `heartmonitor` package."""
import pytest
from heartmonitor import argv_parser


def test_argv_parse_1(capsys):
    res = argv_parser.parse(["--test", "hello"], "--test")
    assert "hello" == res


def test_argv_parse_2(capsys):
    happend = False
    try:
        argv_parser.parse(["--test", "hello"], "--test2")
    except NameError:
        happend = True
    assert happend

def test_argv_parse_3(capsys):
    happend = False
    try:
        argv_parser.parse([], "--test2")
    except NameError:
        happend = True
    assert happend

def test_argv_parse_4(capsys):
    happend = False
    try:
        argv_parser.parse([], "")
    except NameError:
        happend = True
    assert happend

def test_argv_parse_5(capsys):
    happend = False
    try:
        argv_parser.parse(["--test"], "--test")
    except ValueError:
        happend = True
    assert happend


def test_argv_parse_multiple(capsys):
    res = argv_parser.parse_multiple(["--test", "hi", "--key","world"], ["--test", "--key"])
    assert "--test" in res
    assert "--key" in res
    assert res["--test"] == "hi"
    assert res["--key"] == "world"
    assert len(res.keys()) == 2

def test_argv_parse_multiple_2(capsys):
    res = argv_parser.parse_multiple(["--test", "hi", "--key","world"], ["--test"])
    assert "--test" in res
    assert res["--test"] == "hi"
    assert len(res.keys()) == 1

def test_argv_parse_multiple_3(capsys):
    happend = False
    try:
        argv_parser.parse_multiple(["--test", "hi", "--key","world"], ["--te2st", "--key"])
    except NameError:
        happend = True
    assert happend

def test_argv_parse_multiple_4(capsys):
    happend = False
    try:
        argv_parser.parse_multiple(["--test", "hi", "--key",], ["--test", "--key"])
    except ValueError:
        happend = True
    assert happend
