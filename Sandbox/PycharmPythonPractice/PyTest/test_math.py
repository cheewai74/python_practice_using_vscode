import pytest


@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2


@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c


@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)


@pytest.mark.math
def test_multiply_two_positive_ints():
    assert 2 * 3 == 6


@pytest.mark.math
def test_multiply_identity():
    assert 1 * 99 == 99


@pytest.mark.math
def test_multiply_zero():
    assert 0 * 100 == 0


products = [
    (2, 3, 6),  # postive integers
    (1, 99, 99),  # identity
    (0, 99, 0),  # zero
    (3, -4, -12),  # positive by negative
    (-5, -5, 25),  # negative by negative
    (2.5, 6.7, 16.75)  # floats
]


@pytest.mark.parametrize('a, b, products', products)
def test_multiplication(a, b, products):
    assert a * b == products
