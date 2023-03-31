import pytest

from app.Calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 5) == 10

    def test_devision_success(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 10, 4) == 6

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_adding_success_secondtest(self):
        assert self.calc.adding(self, 5, 5) == 10

    def test_multiply_success_secondtest(self):
        assert self.calc.multiply(self, 10, 2) == 20

    def test_devision_success_seconttest(self):
        assert self.calc.division(self, 40, 5) == 8

    def test_subtraction_success_secondtest(self):
        assert self.calc.subtraction(self, 20, 5) == 15

    def test_zero_division_secondtest(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 5, 0)

    def teardown(self):
        print('Выполнение метода teardown')

