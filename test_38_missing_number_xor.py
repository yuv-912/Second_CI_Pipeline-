import importlib

module = importlib.import_module("38_missing_number_xor")


def test_missing_in_zero_to_n():
    assert module.find_missing_number([3, 0, 1]) == 2


def test_missing_last_element():
    assert module.find_missing_number([0, 1]) == 2


def test_larger_range():
    assert module.find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_range_starting_from_one():
    assert module.find_missing_number([1, 2, 4, 5]) == 3
