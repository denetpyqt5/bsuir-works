import pytest
from ppois.first.src.input import ValidInput

vi = ValidInput()

@pytest.mark.parametrize("raw, left, right, expected", [
    ("5",  1, 10, 5),
    ("1",  1, 10, 1),
    ("10", 1, 10, 10),
    ("0",  1, 10, None),
    ("11", 1, 10, None),
    ("abc",1, 10, None),
    ("",   1, 10, None),
])
def test_parse(raw, left, right, expected):
    assert vi._parse(raw, left, right) == expected