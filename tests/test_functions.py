import pytest


# --- Sample functions ---
def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def get_status_code(status):
    if status == "OK":
        return 200
    return 404


# --- The Tests ---


def test_simple_assertion():
    result = get_status_code("OK")
    assert result == 200


# Table-Driven Tests (Go style: []struct{name, input, want})
# In Python, we use the @pytest.mark.parametrize decorator.
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("OK", 200),
        ("MISSING", 404),
        ("ERROR", 404),
    ],
)
def test_status_codes_table(input_str, expected):
    assert get_status_code(input_str) == expected


# Testing Errors/Panics
def test_divide_by_zero():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        divide(10, 0)


# Floating Point Comparison
def test_float_precision():
    result = 0.1 + 0.2
    # assert result == 0.3  <-- This would fail due to float precision
    assert result == pytest.approx(0.3)
