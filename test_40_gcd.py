import importlib

module = importlib.import_module("40_gcd")


def test_standard_numbers():
    assert module.gcd(48, 18) == 6


def test_coprime_numbers():
    assert module.gcd(17, 13) == 1


def test_with_zero():
    assert module.gcd(0, 5) == 5
    assert module.gcd(10, 0) == 10


def test_same_numbers():
    assert module.gcd(25, 25) == 25


def test_negative_numbers():
    assert module.gcd(-48, 18) == 6
