import pytest
from arg_test import get_primes


@pytest.mark.parametrize(
    "num1, num2, expected_primes",
    [
        (1, 10, [2, 3, 5, 7]),
        # (1, 10, [2, 3, 5, 9]), # invalid test/breaking test
        (10, 30, [11, 13, 17, 19, 23, 29]),
        (20, 50, [23, 29, 31, 37, 41, 43, 47]),
    ],
)
def test_func(num1: int, num2: int, expected_primes: int):
    assert get_primes(num1, num2) == expected_primes
