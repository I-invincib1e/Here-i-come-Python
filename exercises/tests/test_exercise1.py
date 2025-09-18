import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from exercise1 import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_five():
    assert factorial(5) == 120

def test_factorial_ten():
    assert factorial(10) == 3628800

if __name__ == "__main__":
    test_factorial_zero()
    test_factorial_one()
    test_factorial_five()
    test_factorial_ten()
    print("All tests passed!")
