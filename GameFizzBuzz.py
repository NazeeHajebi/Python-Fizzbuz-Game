def fizz_buzz(number):
    def divisible_by(n):
        return number%n ==0

    if divisible_by(15):
        return "fizzbuzz"
    elif divisible_by(3):
        return "fizz"
    elif divisible_by(5):
        return "buzz"
    return str(number)