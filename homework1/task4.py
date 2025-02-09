import pytest

def calculate_discount(price, discount):
    if discount > 1:
        return price * (discount * .01)
    return price * discount


def test_calculate_discount():
    #int
    assert calculate_discount(50, 50) == 50 * .5
    #float percentage
    assert calculate_discount(50, 0.5) == 50 * .5
    #float 
    assert calculate_discount(30.25, 25.23) == 30.25 * 0.2523 
    assert calculate_discount(30.25, .2523) == 30.25 * 0.2523 