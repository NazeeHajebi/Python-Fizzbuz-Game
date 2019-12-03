from GameFizzBuzz import fizz_buzz


def test_answer():
    check(1, "1")
    check(2, "2")
    check(3, "fizz")
    check(5, "buzz")
    check(15,"fizzbuzz")



def check(number, expected_result):
    assert fizz_buzz(number) == expected_result



