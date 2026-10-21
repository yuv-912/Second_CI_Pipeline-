import importlib

module = importlib.import_module("36_most_frequent")


def test_standard_numbers():
    assert module.most_frequent([1, 3, 2, 1, 4, 1]) == 1


def test_string_elements():
    assert module.most_frequent(["apple", "banana", "apple"]) == "apple"


def test_single_element():
    assert module.most_frequent([42]) == 42


def test_empty_list():
    assert module.most_frequent([]) is None
