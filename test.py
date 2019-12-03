import pytest


def fizz_buzz(number):
    if number %3 == 0:
        return "fizz"
    elif number %5 == 0:
        return "buzz"

    return str(number)


def test_answer():
    check(1, "1")
    check(2, "2")
    check(3, "fizz")
    check(5, "buzz")



def check(number, expected_result):
    assert fizz_buzz(number) == expected_result



