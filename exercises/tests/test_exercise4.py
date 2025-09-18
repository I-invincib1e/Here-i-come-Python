import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from exercise4 import find_max

def test_find_max_normal():
    assert find_max([1, 3, 2, 5, 4]) == 5

def test_find_max_single():
    assert find_max([42]) == 42

def test_find_max_negative():
    assert find_max([-1, -3, -2]) == -1

def test_find_max_empty():
    assert find_max([]) is None

if __name__ == "__main__":
    test_find_max_normal()
    test_find_max_single()
    test_find_max_negative()
    test_find_max_empty()
    print("All tests passed!")
