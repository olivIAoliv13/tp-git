from calculator import addition
from calculator import division
from calculator import substraction

def test_addition():
    assert addition(1, 2) == 3

def test_division():
    assert division(4,2) == 2

def test_substraction():
    assert substraction(8, 7) == 1
