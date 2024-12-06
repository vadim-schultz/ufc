import pytest
from example.implementation import to_roman, from_roman


@pytest.mark.parametrize(
    "integer, roman",
    [
        (1, "I"),
        (4, "IV"),
        (9, "IX"),
        (10, "X"),
        (40, "XL"),
        (90, "XC"),
        (400, "CD"),
        (900, "CM"),
        (1000, "M"),
        (1987, "MCMLXXXVII"),
        (2022, "MMXXII"),
        (3000, "MMM"),
    ],
)
def test_to_roman(integer, roman):
    assert to_roman(integer) == roman


@pytest.mark.parametrize(
    "roman, integer",
    [
        ("I", 1),
        ("IV", 4),
        ("IX", 9),
        ("X", 10),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("M", 1000),
        ("MCMLXXXVII", 1987),
        ("MMXXII", 2022),
        ("MMM", 3000),
    ],
)
def test_from_roman(roman, integer):
    assert from_roman(roman) == integer


@pytest.mark.parametrize("integer", range(1, 3001))
def test_round_trip_integer_to_roman(integer):
    assert from_roman(to_roman(integer)) == integer


@pytest.mark.parametrize(
    "roman",
    [
        "I",
        "IV",
        "IX",
        "XL",
        "XC",
        "CD",
        "CM",
        "M",
        "MCMLXXXVII",
        "MMXXII",
        "MMM",
    ],
)
def test_round_trip_roman_to_integer(roman):
    assert to_roman(from_roman(roman)) == roman


@pytest.mark.parametrize(
    "invalid_roman",
    [
        "",          # Empty string
        "IIII",      # Too many repeats
        "VV",        # Invalid repetition
        "IC",        # Invalid subtraction
        "XM",        # Invalid subtraction
        "MMMX",      # Too large
        "123",       # Contains non-Roman characters
        "ABC",       # Invalid characters
    ],
)
def test_invalid_roman_numerals(invalid_roman):
    with pytest.raises(ValueError):
        from_roman(invalid_roman)


@pytest.mark.parametrize(
    "invalid_integer",
    [-1, 0, 3001, "string", None]  # Values out of range and non-integer types.
)
def test_invalid_integer_to_roman(invalid_integer):
    with pytest.raises(ValueError):
        to_roman(invalid_integer)
