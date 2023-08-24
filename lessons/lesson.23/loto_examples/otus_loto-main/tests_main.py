import pytest
from pytest import fixture

from main import loto_utils
count = 80
min = 0
max = 100

@fixture
def input_count() -> int:
    input = 80
    return input

def test_input_correct(input_count: int):
    current = loto_utils.generate_unique_numbers(input_count, min, max)
    assert input_count == len(current)

def test_inputValueError():
    with pytest.raises(ValueError):
        loto_utils.generate_unique_numbers(10000, 100, 100)

def test_countzero():
    assert len(loto_utils.generate_unique_numbers(0, 100, 200)) == 0

def test_positiveinput_correctvalues():
    actual = loto_utils.generate_unique_numbers(count, min, max)
    for item in actual:
        assert (min <= item <= max)

