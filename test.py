import pytest


def fizz_buzz(number):
    if number%15 ==0:
        return "fizzbuzz"
    elif number %3 == 0:
        return "fizz"
    elif number %5 == 0:
        return "buzz"



    return str(number)


def test_answer():
    check(1, "1")
    check(2, "2")
    check(3, "fizz")
    check(5, "buzz")
    check(15,"fizzbuzz")



def check(number, expected_result):
    assert fizz_buzz(number) == expected_result



