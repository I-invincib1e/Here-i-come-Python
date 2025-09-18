import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from exercise2 import is_prime

def test_is_prime_two():
    assert is_prime(2) == True

def test_is_prime_three():
    assert is_prime(3) == True

def test_is_prime_seven():
    assert is_prime(7) == True

def test_is_prime_four():
    assert is_prime(4) == False

def test_is_prime_one():
    assert is_prime(1) == False

def test_is_prime_zero():
    assert is_prime(0) == False

if __name__ == "__main__":
    test_is_prime_two()
    test_is_prime_three()
    test_is_prime_seven()
    test_is_prime_four()
    test_is_prime_one()
    test_is_prime_zero()
    print("All tests passed!")
