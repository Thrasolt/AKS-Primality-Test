import math
import enum

from number_theory import is_co_prime, order, get_next_co_prime, phi
from polynomial_fermat import check_single_polynomial_congruence


class Property(enum.Enum):
    COMPOSITE = 0
    PRIME = 1


def find_r(number: int,  upper_limit) -> int:
    r: int = get_next_co_prime(number, 2)
    while order(number, r) < upper_limit:
        r = get_next_co_prime(number, r+1)
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
            power += 1
    return False


def calculate_limit_for_general_fermat(number: int, r: int) -> int:
    return math.floor(math.sqrt(phi(r)) * math.log2(number))


def check_polynomial_fermat(number: int, r: int) -> Property:
    upper_limit: int = calculate_limit_for_general_fermat(number, r)
    for constant_term in range(1, upper_limit + 1):
        if not check_single_polynomial_congruence(number, r, constant_term):
            return Property.COMPOSITE
    return Property.PRIME


def aks_primality(number: int) -> Property:
    assert number > 1, "The input number must be greater than 1"
    if is_perfect_power(number):
        return Property.COMPOSITE

    r = find_r(number, upper_limit=math.log2(number)**2)

    if has_non_trivial_gcd(number, r):
        return Property.COMPOSITE

    return check_polynomial_fermat(number, r)


if __name__ == '__main__':
    print(aks_primality(7919))
    print(aks_primality(933199))
