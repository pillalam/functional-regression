from calculator import Calculator
from nose.tools import assert_equal


class TestCalculator(object):
    def test_add(self):
        a = Calculator()
        assert_equal(a.add(3, 4), 7)

    def test_subtract(self):
        a = Calculator()
        assert_equal(a.subtract(4, 3), 1)

    def test_multiply(self):
        a = Calculator()
        assert_equal(a.multiply(4, 3), 12)

    def test_divide(self):
        a = Calculator()
        assert_equal(a.divide(4, 2), 2)
