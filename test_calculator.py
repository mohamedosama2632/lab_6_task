import pytest
from calculator import Calculator


# Testing addition
def test_add_1():
    calc = Calculator(5, 3)
    assert calc.add() == 8

def test_add_2():
    calc = Calculator(10, 20)
    assert calc.add() == 30

def test_add_3():
    calc = Calculator(-5, 2)
    assert calc.add() == -3


# Testing subtraction
def test_subtract_1():
    calc = Calculator(10, 5)
    assert calc.subtract() == 5

def test_subtract_2():
    calc = Calculator(5, 10)
    assert calc.subtract() == -5

def test_subtract_3():
    calc = Calculator(-5, -3)
    assert calc.subtract() == -2


# Testing multiplication
def test_multiply_1():
    calc = Calculator(4, 3)
    assert calc.multiply() == 12

def test_multiply_2():
    calc = Calculator(5, 0)
    assert calc.multiply() == 0

def test_multiply_3():
    calc = Calculator(-2, 3)
    assert calc.multiply() == -6


# Testing division
def test_divide_1():
    calc = Calculator(10, 2)
    assert calc.divide() == 5

def test_divide_2():
    calc = Calculator(9, 3)
    assert calc.divide() == 3

def test_divide_3():
    calc = Calculator(5, 0)
    with pytest.raises(ValueError):
        calc.divide()
