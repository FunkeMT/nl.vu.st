import pytest
import output_parser
import entity
import os


def test_output_parse(capsys):
    m = entity.Measurement(90, 100, 110, 120)
    mr = entity.MeasurementResult(
        m,
        entity.StatusEnum.MINOR,
        entity.StatusEnum.OK,
        entity.StatusEnum.LIFE_THREATENING,
        entity.StatusEnum.MAJOR,
    )

    output = output_parser.format_status(mr)
    assert "90" in output
    assert "100" in output
    assert "110" in output
    assert "120" in output


def test_output_parse2(capsys):
    m = entity.Measurement(90, 100, 110, 120)
    mr = entity.MeasurementResult(
        m,
        entity.StatusEnum.MISSING,
        entity.StatusEnum.OK,
        entity.StatusEnum.LIFE_THREATENING,
        entity.StatusEnum.MAJOR,
    )
    res = output_parser.format_status(mr)
    assert "0" in res
    assert "100" in res
    assert "110" in res
    assert "120" in res
    assert "MISSING" in res
    assert "OK" in res
    assert "LIFE_THREATENING" in res
    assert "MAJOR" in res


def test_output_parse3(capsys):
    m = entity.Measurement(90, 100, 110, 120)
    mr = entity.MeasurementResult(
        m,
        entity.StatusEnum.OK,
        entity.StatusEnum.MISSING,
        entity.StatusEnum.OK,
        entity.StatusEnum.OK,
    )
    res = output_parser.format_status(mr)
    assert "90" in res
    assert "110" in res
    assert "120" in res
    assert "MISSING" in res
    assert "OK" in res


def test_output_parse4(capsys):
    m = entity.Measurement(90, 100, 110, 120)
    mr = entity.MeasurementResult(
        m,
        entity.StatusEnum.OK,
        entity.StatusEnum.OK,
        entity.StatusEnum.MISSING,
        entity.StatusEnum.OK,
    )
    res = output_parser.format_status(mr)
    assert "100" in res
    assert "90" in res
    assert "120" in res
    assert "OK" in res
    assert "MISSING" in res


def test_output_parse5(capsys):
    m = entity.Measurement(90, 100, 110, 120)
    mr = entity.MeasurementResult(
        m,
        entity.StatusEnum.OK,
        entity.StatusEnum.OK,
        entity.StatusEnum.OK,
        entity.StatusEnum.MISSING,
    )
    res = output_parser.format_status(mr)
    assert "0 mm Hg," in res
    assert "100" in res
    assert "90" in res
    assert "110" in res
    assert "MISSING" in res
    assert "OK" in res


def test_format_statistics(capsys):
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
