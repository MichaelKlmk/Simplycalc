import pytest

from main import add, divide, multiply, subtract


class TestClass:


    @pytest.fixture()
    def numbers(self):
        x = 10
        y = 20
        z = 30
        return [x, y, z]

    def test_add2(self, numbers):
        x = numbers[0]
        y = numbers[1]
        z = numbers[2]
        assert add(x, y) == z

    @pytest.mark.parametrize("x, y, z", [(1, 1, 2), (1.5, 0.5, 2), (10, 100, 110)])
    def test_add(self, x, y, z):
        assert add(x, y) == z

    @pytest.mark.parametrize("x, y, z", [(2, 1, 1), (2, 0.5, 1.5), (110, 100, 10)])
    def test_subtract(self, x, y, z):
        assert subtract(x, y) == z

    @pytest.mark.parametrize("x, y, z", [(10, 1, 10), (2, 0.5, 1), (110, 100, 11000)])
    def test_multiply(self, x, y, z):
        assert multiply(x, y) == z

    @pytest.mark.xfail
    @pytest.mark.parametrize("x, y, z", [(2, 1, 2), (2, 0.5, 4), (110, 110, 1)])
    def test_divide(self, x, y, z):
        assert divide(x, y) == z






