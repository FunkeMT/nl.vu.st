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


def test_help(capsys):
    """Correct name argument and printing"""
    main.print_help()
    captured = capsys.readouterr()
    lines = captured.out.split("\n")
    assert "Command usage is as follows:" == lines[0]
    assert "heartbeatmonitor.py arguments:" == lines[1]
    assert "" == lines[2]
    assert "Arguments are the following:" == lines[3]
    assert "  --age number\tAge of the patient" == lines[4]
    assert "  --height whole-number\tHeight of the patient" == lines[5]
    assert "  --weight whole-number\tWeight of the patient" == lines[6]
    assert "  --gender text\tGender of the patient. Supported values (capital insensitve): male, female" == lines[7]
