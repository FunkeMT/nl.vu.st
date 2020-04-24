import pytest
import output_parser
import entity

def test_output_parse(capsys):
    m = entity.Measurement(90, 100 ,110 ,120)
    mr = entity.MeasurementResult(m)
    res = output_parser.print_status(mr)
    captured = capsys.readouterr()
    assert "90"  in captured.out
    assert "100"  in captured.out
    assert "110"  in captured.out
    assert "120"  in captured.out

def test_output_parse(capsys):
    m = entity.Measurement(90, 100 ,110 ,120)
    mr = entity.MeasurementResult(m, entity.StatusEnum.MISSING, entity.StatusEnum.OK, entity.StatusEnum.LIFE_THREATENING, entity.StatusEnum.MAJOR)
    res = output_parser.print_status(mr)
    captured = capsys.readouterr()
    assert "90"  in captured.out
    assert "100"  in captured.out
    assert "110"  in captured.out
    assert "120" in captured.out
    assert "MISSING" in captured.out
    assert "OK" in captured.out
    assert "MAJOR" in captured.out
    assert "LIFE_THREATENING" in captured.out

 
