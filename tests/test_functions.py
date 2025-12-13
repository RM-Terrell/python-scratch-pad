import pytest

import main.functions as functions


def test_simple_assertion():
    result = functions.get_status_code("OK")
    assert result == 200


def test_negative_zero():
    result = functions.negative(0)
    assert result == 0


def test_negative_negative():
    result = functions.negative(-1)
    assert result == -1


def test_negative_positive():
    result = functions.negative(1)
    assert result == -1


# Table-Driven Tests
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("OK", 200),
        ("MISSING", 404),
        ("ERROR", 404),
    ],
)
def test_status_codes_table(input_str, expected):
    assert functions.get_status_code(input_str) == expected


# Testing Errors/Panics
def test_divide_by_zero():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        functions.divide(10, 0)


# Floating Point Comparison
def test_float_precision():
    result = 0.1 + 0.2
    # assert result == 0.3  <-- This would fail due to float precision
    assert result == pytest.approx(0.3)
