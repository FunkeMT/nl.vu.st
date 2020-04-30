"""Tests for `heartmonitor.entity` package."""
import pytest
import entity


def test_StatusEnum(capsys):
    """Testing entity StatusEnum"""
    data = entity.StatusEnum.__dict__
    keys = []
    for k in data:
        if k.startswith("_"):
            continue
        keys.append(k)

    assert "OK" in keys
    assert "MISSING" in keys
    assert "MINOR" in keys
    assert "MAJOR" in keys
    assert "LIFE_THREATENING" in keys

    assert entity.StatusEnum.OK.value == "OK"
    assert entity.StatusEnum.MISSING.value == "MISSING"
    assert entity.StatusEnum.MINOR.value == "MINOR"
    assert entity.StatusEnum.MAJOR.value == "MAJOR"
    assert entity.StatusEnum.LIFE_THREATENING.value == "LIFE_THREATENING"

    assert 5 == len(keys)


def test_Measurement(capsys):
    """Testing entity Measurement"""
    m = entity.Measurement()

    assert m.oxygen is None
    assert m.pulse is None
    assert m.blood_pressure_systolic is None
    assert m.blood_pressure_diastolic is None


def test_MeasurementValues(capsys):
    """Testing entity MeasurementValues"""
    m = entity.Measurement(10, 20, 30, 40)

    assert m.oxygen == 10
    assert m.pulse == 20
    assert m.blood_pressure_systolic == 30
    assert m.blood_pressure_diastolic == 40


def test_MeasurementResult(capsys):
    """Testing entity MeasurementResult"""
    m = entity.Measurement()
    mr = entity.MeasurementResult(m)

    assert mr.oxygen_status is entity.StatusEnum.MISSING
    assert mr.pulse_status is entity.StatusEnum.MISSING
    assert mr.blood_pressure_systolic_status is entity.StatusEnum.MISSING
    assert mr.blood_pressure_diastolic_status is entity.StatusEnum.MISSING
    assert mr.m is m


def test_MeasurementResultValues(capsys):
    """Testing entity MeasurementResultValues"""
    m = entity.Measurement(10, 20, 30, 40)
    mr = entity.MeasurementResult(
        m,
        entity.StatusEnum.MISSING,
        entity.StatusEnum.OK,
        entity.StatusEnum.MINOR,
        entity.StatusEnum.MAJOR,
    )

    assert mr.oxygen_status == entity.StatusEnum.MISSING
    assert mr.pulse_status == entity.StatusEnum.OK
    assert mr.blood_pressure_systolic_status == entity.StatusEnum.MINOR
    assert mr.blood_pressure_diastolic_status == entity.StatusEnum.MAJOR


def test_AbstractRecording(capsys):
    """Testing entity AbstractRecording"""
    ar = entity.AbstractRecording()

    assert isinstance(ar.get_iterator(), entity.AbstractRecording)

    happend = False
    try:
        ar.__next__()
    except StopIteration:
        happend = True
    assert happend

    assert ar == ar.__iter__()


def test_FileRecording(capsys):
    """Testing FileRecording"""
    entity.FileRecording("heartmonitor/tests/test_files/file_recording/heading_ok.csv")
    assert True


def test_FileRecording2(capsys):
    """Testing FileRecording"""
    happend = False
    try:
        entity.FileRecording(
            "heartmonitor/tests/test_files/file_recording/heading_missing_1.csv"
        )
    except AssertionError:
        happend = True
    assert happend


def test_FileRecording3(capsys):
    """Testing FileRecording"""
    happend = False
    try:
        entity.FileRecording(
            "heartmonitor/tests/test_files/file_recording/heading_missing_2.csv"
        )
    except AssertionError:
        happend = True
    assert happend


def test_FileRecording4(capsys):
    """Testing FileRecording"""
    happend = False
    try:
        entity.FileRecording(
            "heartmonitor/tests/test_files/file_recording/heading_missing_3.csv"
        )
    except AssertionError:
        happend = True
    assert happend


def test_FileRecording5(capsys):
    """Testing FileRecording"""
    happend = False
    try:
        entity.FileRecording(
            "heartmonitor/tests/test_files/file_recording/heading_missing_4.csv"
        )
    except AssertionError:
        happend = True
    assert happend


def test_FileRecording6(capsys):
    """Testing FileRecording"""
    happend = False
    try:
        entity.FileRecording(
            "heartmonitor/tests/test_files/file_recording/heading_missing_5.csv"
        )
    except AssertionError:
        happend = True
    assert happend


def test_FileRecording7(capsys):
    """Testing FileRecording"""
    happend = False
    try:
        entity.FileRecording(
            "heartmonitor/tests/test_files/file_recording/heading_missing_6.csv"
        )
    except AssertionError:
        happend = True
    assert happend


def test_FileRecording8(capsys):
    """Testing FileRecording"""
    happend = False  # type: entity.FileRecording
    fr = None
    msg = ""
    try:
        fr = entity.FileRecording(
            "heartmonitor/tests/test_files/file_recording/not_existing.csv"
        )
    except entity.FileNotFound as ex:
        msg = str(ex)
        happend = True
    assert happend
    assert fr is None
    assert msg == "Could not find recording file."


def test_FileRecording9(capsys):
    """Testing FileRecording"""
    happend = False
    try:
        fr = entity.FileRecording(
            "heartmonitor/tests/test_files/file_recording/heading_missing_7.csv"
        )
        fr.__iter__().__next__()
    except StopIteration:
        happend = True
    assert happend


def test_FileRecording10(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_1.csv")
    assert True

    it = fr.get_iterator()
    assert fr == it

    counter = 0
    for x in it:
        assert x.oxygen == 1
        assert x.pulse == 2
        assert x.blood_pressure_systolic == 3
        assert x.blood_pressure_diastolic == 4
        counter += 1

    assert counter == 1


def test_FileRecording11(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_2.csv")
    assert True

    it = fr.get_iterator()
    assert fr == it

    counter = 0
    for x in it:
        assert x.oxygen == 1
        assert x.pulse == 2
        assert x.blood_pressure_systolic == 3
        assert x.blood_pressure_diastolic is None
        counter += 1

    assert counter == 1


def test_FileRecording12(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_3.csv")
    assert True

    it = fr.get_iterator()
    assert fr == it

    counter = 0
    for x in it:
        assert x.oxygen == 1
        assert x.pulse == 2
        assert x.blood_pressure_systolic is None
        assert x.blood_pressure_diastolic == 4
        counter += 1

    assert counter == 1


def test_FileRecording13(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_4.csv")
    assert True

    it = fr.get_iterator()
    assert fr == it

    counter = 0
    for x in it:
        assert x.oxygen == 1
        assert x.pulse is None
        assert x.blood_pressure_systolic == 3
        assert x.blood_pressure_diastolic == 4
        counter += 1

    assert counter == 1


def test_FileRecording14(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_5.csv")
    assert True

    it = fr.get_iterator()
    assert fr == it

    counter = 0
    for x in it:
        assert x.oxygen is None
        assert x.pulse == 2
        assert x.blood_pressure_systolic == 3
        assert x.blood_pressure_diastolic == 4
        counter += 1

    assert counter == 1


def test_FileRecording15(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_6.csv")
    assert True

    it = fr.get_iterator()
    assert fr == it

    counter = 0
    for x in it:
        assert x.oxygen is None
        assert x.pulse is None
        assert x.blood_pressure_systolic is None
        assert x.blood_pressure_diastolic is None
        counter += 1

    assert counter == 1


def test_FileRecording16(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    assert True

    it = fr.get_iterator()
    assert fr == it

    counter = 0
    for _ in it:
        counter += 1

    assert counter == 0


def test_FileRecording17(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    assert True

    fp = fr._fpointer

    # Destuct the file recording.
    fr = None

    assert fp.closed


def test_FileRecording18(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    assert True
    res = list(fr._get_indices(["a", "b"], ["a", "b"]))
    assert res[0] == 0
    assert res[1] == 1


def test_FileRecording19(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    assert True
    res = list(fr._get_indices(["b", "a"], ["a", "b"]))
    assert res[0] == 1
    assert res[1] == 0


def test_FileRecording20(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    assert True
    res = list(fr._get_indices(["b", "a", "c"], ["a", "b"]))
    assert res[0] == 1
    assert res[1] == 0


def test_FileRecording21(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    assert True
    res = list(fr._get_indices(["b", "a", "c"], ["a", "b", "c"]))
    assert res[0] == 1
    assert res[1] == 0
    assert res[2] == 2


def test_FileRecording22(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    fr._validate_heading(
        ["oxygen", "pulse", "blood_pressure_systolic", "blood_pressure_diastolic"]
    )
    assert True


def test_FileRecording23(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._validate_heading([])
    except AssertionError:
        happend = True
    assert happend


def test_FileRecording24(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._validate_heading(["oxygen"])
    except AssertionError:
        happend = True
    assert happend


def test_FileRecording25(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._validate_heading(
            ["a", "pulse", "blood_pressure_systolic", "blood_pressure_diastolic"]
        )
    except AssertionError:
        happend = True
    assert happend


def test_FileRecording26(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._validate_heading(
            ["oxygen", "a", "blood_pressure_systolic", "blood_pressure_diastolic"]
        )
    except AssertionError:
        happend = True
    assert happend


def test_FileRecording27(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._validate_heading(["oxygen", "pulse", "a", "blood_pressure_diastolic"])
    except AssertionError:
        happend = True
    assert happend


def test_FileRecording28(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._validate_heading(["oxygen", "pulse", "blood_pressure_systolic", "a"])
    except AssertionError:
        happend = True
    assert happend


def test_FileRecording29(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    m = fr._line_to_measurement(
        ["1", "2", "3", "4"], make_invalid_measurement_missing=True
    )
    assert isinstance(m, entity.Measurement)
    assert m.oxygen == 1
    assert m.pulse == 2
    assert m.blood_pressure_systolic == 3
    assert m.blood_pressure_diastolic == 4


def test_FileRecording30(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    r = fr._line_to_measurement(
        ["1", "2", "3", "a"], make_invalid_measurement_missing=True
    )
    assert r.blood_pressure_diastolic is None


def test_FileRecording31(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    r = fr._line_to_measurement(
        ["1", "2", "a", "4"], make_invalid_measurement_missing=True
    )
    assert r.blood_pressure_systolic is None


def test_FileRecording32(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    r = fr._line_to_measurement(
        ["1", "a", "3", "4"], make_invalid_measurement_missing=True
    )
    assert r.pulse is None


def test_FileRecording33(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    r = fr._line_to_measurement(
        ["a", "2", "3", "4"], make_invalid_measurement_missing=True
    )
    assert r.oxygen is None


def test_FileRecording34(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._line_to_measurement(
            ["a", "2", "3", "4"], make_invalid_measurement_missing=False
        )
    except ValueError:
        happend = True
    assert happend


def test_FileRecording35(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._line_to_measurement([], make_invalid_measurement_missing=False)
    except IndexError:
        happend = True
    assert happend


def test_FileRecording36(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    m = fr._line_to_measurement(
        ["", "", "", ""], make_invalid_measurement_missing=False
    )
    assert m.blood_pressure_diastolic is None
    assert m.blood_pressure_systolic is None
    assert m.oxygen is None
    assert m.pulse is None


def test_FileRecording37(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    m = fr._line_to_measurement(
        ["1", "2", "3", "4"], make_invalid_measurement_missing=False
    )
    assert isinstance(m, entity.Measurement)
    assert m.oxygen == 1
    assert m.pulse == 2
    assert m.blood_pressure_systolic == 3
    assert m.blood_pressure_diastolic == 4


def test_FileRecording38(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._line_to_measurement(
            ["1", "2", "3", "a"], make_invalid_measurement_missing=False
        )
    except ValueError:
        happend = True
    assert happend


def test_FileRecording39(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._line_to_measurement(
            ["1", "2", "a", "4"], make_invalid_measurement_missing=False
        )
    except ValueError:
        happend = True
    assert happend


def test_FileRecording40(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._line_to_measurement(
            ["1", "a", "3", "4"], make_invalid_measurement_missing=False
        )
    except ValueError:
        happend = True
    assert happend


def test_FileRecording41(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._line_to_measurement(
            ["a", "2", "3", "4"], make_invalid_measurement_missing=False
        )
    except ValueError:
        happend = True
    assert happend


def test_FileRecording42(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._line_to_measurement(
            ["a", "2", "3", "4"], make_invalid_measurement_missing=False
        )
    except ValueError:
        happend = True
    assert happend


def test_FileRecording43(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._line_to_measurement([], make_invalid_measurement_missing=False)
    except IndexError:
        happend = True
    assert happend


def test_FileRecording44(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    m = fr._line_to_measurement(
        ["", "", "", ""], make_invalid_measurement_missing=False
    )
    assert m.blood_pressure_diastolic is None
    assert m.blood_pressure_systolic is None
    assert m.oxygen is None
    assert m.pulse is None


def test_FileRecording45(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    assert (
        fr._parse_field(["0", "54", "a"], 0, make_invalid_measurement_missing=True) == 0
    )
    assert (
        fr._parse_field(["0", "54", "a"], 1, make_invalid_measurement_missing=True)
        == 54
    )
    assert (
        fr._parse_field(["0", "54", "a"], 2, make_invalid_measurement_missing=True)
        is None
    )


def test_FileRecording46(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    assert (
        fr._parse_field(["0", "54", "a"], 0, make_invalid_measurement_missing=False)
        == 0
    )
    assert (
        fr._parse_field(["0", "54", "a"], 1, make_invalid_measurement_missing=False)
        == 54
    )
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._parse_field(["0", "54", "a"], 2, make_invalid_measurement_missing=False)
    except ValueError:
        happend = True
    assert happend


def test_FileRecording47(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._parse_field(["0", "54", "a"], 3, make_invalid_measurement_missing=True)
    except (ValueError, IndexError):
        happend = True
    assert not happend


def test_FileRecording48(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._parse_field(["0", "54", "a"], 3, make_invalid_measurement_missing=False)
    except IndexError:
        happend = True
    assert happend


def test_FileRecording49(capsys):
    """Testing FileRecording"""
    happend = False
    fr = entity.FileRecording(
        "heartmonitor/tests/test_files/file_recording/heading_extras_1.csv"
    )
    fr.__iter__().__next__()
    try:
        fr.__iter__().__next__()
    except StopIteration:
        happend = True
    assert happend


def test_FileRecording50(capsys):
    """Testing FileRecording"""
    happend = False
    fr = entity.FileRecording(
        "heartmonitor/tests/test_files/file_recording/heading_extras_2.csv"
    )
    fr.__iter__().__next__()
    try:
        fr.__iter__().__next__()
    except StopIteration:
        happend = True
    assert happend


def test_FileRecording51(capsys):
    """Testing FileRecording"""
    happend = False
    fr = entity.FileRecording(
        "heartmonitor/tests/test_files/file_recording/heading_extras_3.csv"
    )
    fr.__iter__().__next__()
    try:
        fr.__iter__().__next__()
    except StopIteration:
        happend = True
    assert happend


def test_FileRecording52(capsys):
    """Testing FileRecording"""
    happend = False
    fr = entity.FileRecording(
        "heartmonitor/tests/test_files/file_recording/heading_extras_4.csv"
    )
    fr.__iter__().__next__()
    try:
        fr.__iter__().__next__()
    except StopIteration:
        happend = True
    assert happend


def test_FileRecording53(capsys):
    """Testing FileRecording"""
    happend = False
    fr = entity.FileRecording(
        "heartmonitor/tests/test_files/file_recording/heading_extras_5.csv"
    )
    fr.__iter__().__next__()
    try:
        fr.__iter__().__next__()
    except StopIteration:
        happend = True
    assert happend


def test_FileRecording54(capsys):
    """Testing FileRecording"""
    happend = False
    fr = entity.FileRecording(
        "heartmonitor/tests/test_files/file_recording/heading_extras_6.csv"
    )
    fr.__iter__().__next__()
    try:
        fr.__iter__().__next__()
    except StopIteration:
        happend = True
    assert happend


def test_FileRecording55(capsys):
    """Testing FileRecording"""
    happend = False
    fr = entity.FileRecording(
        "heartmonitor/tests/test_files/file_recording/heading_extras_7.csv"
    )
    fr.__iter__().__next__()
    try:
        fr.__iter__().__next__()
    except StopIteration:
        happend = True
    assert happend


def test_FileRecording56(capsys):
    """Testing FileRecording"""
    happend = False
    fr = entity.FileRecording(
        "heartmonitor/tests/test_files/file_recording/heading_extras_8.csv"
    )
    fr.__iter__().__next__()
    try:
        fr.__iter__().__next__()
    except StopIteration:
        happend = True
    assert happend


def test_FileRecording57(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._parse_field(["0", "54", "a"], 2, make_invalid_measurement_missing=True)
    except ValueError:
        happend = True
    assert not happend


def test_FileRecording58(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._parse_field(["0", "54", "a"], 2)
    except ValueError:
        happend = True
    assert happend


def test_FileRecording59(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._line_to_measurement(
            ["a", "2", "3", "4"], make_invalid_measurement_missing=True
        )
    except ValueError:
        happend = True
    assert not happend


def test_FileRecording60(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._line_to_measurement(
            ["a", "2", "3", "4"], make_invalid_measurement_missing=False
        )
    except ValueError:
        happend = True
    assert happend


def test_FileRecording61(capsys):
    """Testing FileRecording"""
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_7.csv")
    happend = False
    try:
        fr._line_to_measurement(["a", "2", "3", "4"])
    except ValueError:
        happend = True
    assert happend


def test_FileRecording62(capsys):
    """Testing FileRecording"""
    happend = False
    data = None  # type: entity.Measurement
    try:
        fr = entity.FileRecording(
            "heartmonitor/tests/test_files/file_recording/data_4.csv"
        )
        data = fr.__iter__().__next__(make_invalid_measurement_missing=True)
    except StopIteration:
        happend = True
    assert not happend
    assert data.pulse is None


def test_FileRecording63(capsys):
    """Testing FileRecording"""
    happend = False
    fr = entity.FileRecording("heartmonitor/tests/test_files/file_recording/data_4.csv")
    data = fr.__iter__().__next__()  # type: entity.Measurement
    assert data.pulse is None


def test_MockRecording(capsys):
    """Testing entity MockRecording"""
    mr = entity.MockRecording([entity.Measurement(10)])

    assert len(mr.results) == 1
    assert mr.results[0].oxygen == 10
    assert mr.results[0].pulse is None

    for x in mr.get_iterator():
        assert mr.results[0] == x

    assert mr.__iter__() == mr.results


def test_MeasurementStatistics(capsys):
    """Testing entity MeasurementStatistics"""
    ms = entity.MeasurementStatistics()

    assert ms.ok_count == 0
    assert ms.missing_count == 0
    assert ms.minor_count == 0
    assert ms.major_count == 0
    assert ms.life_threatening_count == 0


def test_MeasurementStatistics(capsys):
    """Testing entity MeasurementStatistics"""
    ms = entity.MeasurementStatistics(0, 1, 2, 3, 4)

    data = entity.StatusEnum.__dict__
    for k in data:
        if k.startswith("_"):
            continue
        prev_value = ms.__getattribute__(k.lower() + "_count")
        ms.increment(data[k])
        assert prev_value == ms.__getattribute__(k.lower() + "_count") - 1


def test_MeasurementStatistics2(capsys):
    """Testing entity MeasurementStatistics"""
    ms = entity.MeasurementStatistics(10, 11, 12, 13, 14)

    data = entity.StatusEnum.__dict__
    for k in data:
        if k.startswith("_"):
            continue
        prev_value = ms.__getattribute__(k.lower() + "_count")
        ms.increment(data[k])
        assert prev_value == ms.__getattribute__(k.lower() + "_count") - 1


def test_Statistics(capsys):
    """Testing entity Statistics"""
    oxygen = entity.MeasurementStatistics()
    pulse = entity.MeasurementStatistics()
    blood_pressure_systolic = entity.MeasurementStatistics()
    blood_pressure_diastolic = entity.MeasurementStatistics()

    s = entity.Statistics(
        oxygen, pulse, blood_pressure_systolic, blood_pressure_diastolic
    )
    assert s.oxygen == oxygen
    assert s.pulse == pulse
    assert s.blood_pressure_systolic == blood_pressure_systolic
    assert s.blood_pressure_diastolic == blood_pressure_diastolic
