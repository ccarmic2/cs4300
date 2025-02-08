import pytest

def check_num(x):
    if x > 0: 
        return '+'
    if x == 0:
        return '0'
    if x < 0:
        return '-'
    
def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: 
            return False
    return True

def first_ten_prime():
    primes = []
    num = 2
    i = 0
    for i in range(10):
        num += 1
        while is_prime(num) == False:
            num += 1
        primes.append(num)
    return primes

def sum_one_to_hundred():
    sum = 0
    i = 1
    while i <= 100:
        sum += i
        i += 1
    return sum



def test_check_num():
    assert check_num(-2) == '-'
    assert check_num(3) == '+'
    assert check_num(0) == '0'

def test_first_ten_prime():
    assert len(first_ten_prime()) == 10
    assert first_ten_prime() == [3,5,7,11,13,17,19,23,29,31]

def test_sum_one_to_hundred():
    expected_output = sum(range(1,101))
    assert sum_one_to_hundred() == expected_output