"""Tests for `heartmonitor.entity` package."""
import pytest
from heartmonitor import main


def test_get_patient_information(capsys):
    happend = False
    try:
        main.get_patient_information([])
    except NameError:
        happend = True
    assert happend 

def test_get_patient_information_2(capsys):
    happend = False
    try:
        main.get_patient_information(["--age", "10", "--height", "10", "--weight", "10", "--gender"])
    except ValueError:
        happend = True
    assert happend 


def test_get_patient_information_3(capsys):
    main.get_patient_information(["--age", "10", "--height", "10", "--weight", "10", "--gender", "male"])
    assert True

def test_get_patient_information_4(capsys):
    happend = False
    try:
        main.get_patient_information(["--age", "-10", "--height", "10", "--weight", "10", "--gender", "male"])
    except ValueError:
        happend = True
    
    assert happend

def test_get_patient_information_5(capsys):
    happend = False
    try:
        main.get_patient_information(["--age", "10", "--height", "-10", "--weight", "10", "--gender", "male"])
    except ValueError:
        happend = True
    
    assert happend

def test_get_patient_information_6(capsys):
    happend = False
    try:
        main.get_patient_information(["--age", "10", "--height", "10", "--weight", "-10", "--gender", "male"])
    except ValueError:
        happend = True
    
    assert happend

def test_get_patient_information_7(capsys):
    happend = False
    try:
        main.get_patient_information(["--age", "10", "--height", "10", "--weight", "10", "--gender", "asd"])
    except ValueError:
        happend = True
    
    assert happend

def test_get_patient_information_8(capsys):
    main.get_patient_information(["--age", "10", "--height", "10", "--weight", "10", "--gender", "female"])
    assert True
