import pytest
import output_parser
import entity


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
    res = output_parser.print_status(mr)
    captured = capsys.readouterr()
    assert "90" in captured.out
    assert "100" in captured.out
    assert "110" in captured.out
    assert "120" in captured.out
    assert "MISSING" in captured.out
    assert "OK" in captured.out
    assert "MAJOR" in captured.out
    assert "LIFE_THREATENING" in captured.out


def test_print_statistics(capsys):
    oxygen = entity.MeasurementStatistics(1, 2, 3, 4, 5)
    pulse = entity.MeasurementStatistics(10, 20, 30, 40, 50)
    bp = entity.MeasurementStatistics(100, 200, 300, 400, 500)
    s = entity.Statistics(oxygen, pulse, bp)
    output_parser.print_statistics(s)
    captured = capsys.readouterr()
    assert "1;" in captured.out
    assert "2;" in captured.out
    assert "3;" in captured.out
    assert "4;" in captured.out
    assert "5" in captured.out
    assert "10;" in captured.out
    assert "20;" in captured.out
    assert "30;" in captured.out
    assert "40;" in captured.out
    assert "50" in captured.out
    assert "100;" in captured.out
    assert "200;" in captured.out
    assert "300;" in captured.out
    assert "400;" in captured.out
    assert "500" in captured.out
