import pytest


def fizz_buzz(number):
    return str(number)


def test_answer():
    check(1, "1")
    check(2, "2")


def check(number, expected_result):
    assert fizz_buzz(number) == expected_result



