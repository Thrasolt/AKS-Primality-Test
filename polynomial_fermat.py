import numpy as np
from numpy.polynomial import polynomial as np_poly


def create_two_sided_polynomial(size: int, constant_term: int) -> np.ndarray:
    polynomial = np.zeros(size+1)
    polynomial[0], polynomial[size] = 1, constant_term
    return polynomial


def create_binomial(constant_term: int) -> np.ndarray:
    return create_two_sided_polynomial(1, constant_term)


def create_module(r: int) -> np.ndarray:
    return create_two_sided_polynomial(r, -1)


def calculate_polynomial_congruence_rep(
        polynomial: np.ndarray,
        polynomial_module: np.ndarray,
        module: int) -> np.ndarray:
    polynomial_remainder: np.ndarray = np_poly.polydiv(polynomial, polynomial_module)[1]
    remainder: np.ndarray = np_poly.polydiv(polynomial_remainder, np.array(module))[1]
    return remainder


def create_expected_result(number: int, constant_term: int, polynomial_module: np.ndarray) -> np.ndarray:
    polynomial = create_two_sided_polynomial(number, constant_term)
    return calculate_polynomial_congruence_rep(polynomial, polynomial_module, number)


def check_single_polynomial_congruence(number: int, r: int, constant_term: int) -> bool:
    binomial: np.ndarray = create_binomial(constant_term)
    binomial_power: np.ndarray = np_poly.polypow(binomial, number)
    polynomial_module: np.ndarray = create_module(r)

    remainder: np.ndarray = calculate_polynomial_congruence_rep(binomial_power, polynomial_module, number)
    binomial_expected = create_expected_result(number, constant_term, polynomial_module)

    return np.allclose(np.nan_to_num(binomial_expected, nan=0.0), np.nan_to_num(remainder, nan=0.0))
