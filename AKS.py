import math
import enum

class Property(enum.Enum):
    COMPOSITE = 0
    PRIME = 1


def is_co_prime(first: int, second: int) -> bool:
    return math.gcd(first, second) == 1


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


def find_r(number: int,  upper_limit) -> int:
    r: int = 2
    while order(number, r) < upper_limit:
        r += 1
    return r


def has_non_trivial_gcd(number: int, r: int) -> bool:
    for candidate in range(2, r + 1):
        gcd: int = math.gcd(candidate, number)
        if 1 < gcd < number:
            return True
    return False


def is_perfect_power(number: int) -> bool:
    for base in range(2, math.floor(math.sqrt(number)) + 1):
        power: int = 2
        while base**power <= number:
            if base**power == number:
                return True
    return False


def calculate_limit_for_general_fermat(number: int, r: int) -> int:
    return math.floor(math.sqrt(phi(r)) * math.log2(number))


def check_polynomial_fermat(number: int, r: int) -> Property:
    upper_limit: int = calculate_limit_for_general_fermat(number, r)
    for candidate in range(1, upper_limit + 1):
        if False:
            return Property.COMPOSITE
    return Property.PRIME


def is_prime(number: int) -> Property:
    assert number > 1, "The input number must be greater than 1"
    if is_perfect_power(number):
        return Property.COMPOSITE

    r = find_r(number, upper_limit=math.log2(number)**2)

    if has_non_trivial_gcd(number, r):
        return Property.COMPOSITE

    return Property.PRIME
