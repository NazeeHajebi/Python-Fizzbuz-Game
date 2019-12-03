import pytest


def fizz_buzz(number):
    return str(number)


def test_answer():
    assert fizz_buzz(1) == "1"
    assert fizz_buzz(2) == "2"
    


