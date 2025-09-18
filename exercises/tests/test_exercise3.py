import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from exercise3 import reverse_string

def test_reverse_hello():
    assert reverse_string("hello") == "olleh"

def test_reverse_empty():
    assert reverse_string("") == ""

def test_reverse_single():
    assert reverse_string("a") == "a"

def test_reverse_python():
    assert reverse_string("python") == "nohtyp"

if __name__ == "__main__":
    test_reverse_hello()
    test_reverse_empty()
    test_reverse_single()
    test_reverse_python()
    print("All tests passed!")
