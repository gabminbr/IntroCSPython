def fizz(n):
    if (n % 3 == 0):
        return True
    else:
        return False


def buzz(n):
    if (n % 5 == 0):
        return True
    else:
        return False


def fizzbuzz(n):
    if (fizz(n) and buzz(n)):
        return "FizzBuzz"
    elif (fizz(n)):
        return "Fizz"
    elif (buzz(n)):
        return "Buzz"
    else:
        return n
