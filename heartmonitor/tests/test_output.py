import pytest
import output_parser
import entity
import os


def test_output_parse(capsys):
    m = entity.Measurement(90, 100, 110, 120)
    mr = entity.MeasurementResult(m)
    res = output_parser.print_status(mr)
    captured = capsys.readouterr()
    assert "90" in captured.out
    assert "100" in captured.out
    assert "110" in captured.out
    assert "120" in captured.out


def test_output_parse(capsys):
    m = entity.Measurement(90, 100, 110, 120)
    mr = entity.MeasurementResult(
        m,
        entity.StatusEnum.MISSING,
        entity.StatusEnum.OK,
        entity.StatusEnum.LIFE_THREATENING,
        entity.StatusEnum.MAJOR,
    )
    output = output_parser.format_status(mr)
    assert "90" in output
    assert "100" in output
    assert "110" in output
    assert "120" in output
    assert "MISSING" in output
    assert "OK" in output
    assert "MAJOR" in output
    assert "LIFE_THREATENING" in output


def test_print_statistics(capsys):
    oxygen = entity.MeasurementStatistics(1, 2, 3, 4, 5)
    pulse = entity.MeasurementStatistics(10, 20, 30, 40, 50)
    bps = entity.MeasurementStatistics(100, 200, 300, 400, 500)
    bpd = entity.MeasurementStatistics(100, 200, 300, 400, 500)
    s = entity.Statistics(oxygen, pulse, bps, bpd)
    output = output_parser.format_statistics(s)
    assert "1;" in output
    assert "2;" in output
    assert "3;" in output
    assert "4;" in output
    assert "5" in output
    assert "10;" in output
    assert "20;" in output
    assert "30;" in output
    assert "40;" in output
    assert "50" in output
    assert "100;" in output
    assert "200;" in output
    assert "300;" in output
    assert "400;" in output
    assert "500" in output
