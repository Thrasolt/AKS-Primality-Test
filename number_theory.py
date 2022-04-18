import math


def is_co_prime(first: int, second: int) -> bool:
    return math.gcd(first, second) == 1


def get_next_co_prime(fix_number: int, current_number: int) -> int:
    number: int = current_number
    while not is_co_prime(fix_number, number):
        number += 1
    return number


def phi(n):
    count = 1
    for candidate in range(2, n):
        if is_co_prime(candidate, n):
            count += 1
    return count


def order(number: int, base: int) -> int:
    exponent: int = 1
    while number**exponent % base != 1:
        exponent += 1
    return exponent