import pytest
import function


class TestFibonacci:
    def test_1(self):
        assert function.fibonacci(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    def test_2(self):
        assert len(function.fibonacci(-2)) == 0

    def test_3(self):
        assert function.fibonacci(1) == [0]

    def test_4(self):
        assert function.fibonacci(1.9) == []


class TestSort:
    def test_1(self):
        assert function.sort("9 8 7 6 5 4 3 2 1") == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_2(self):
        assert function.sort("0 -1") == [-1, 0]

    def test_3(self):
        assert function.sort("-1 1") == [1, -1]


class TestCalc:
    def test_1(self):
        assert function.calc(1, 2, '+') == 3

    def test_2(self):
        assert function.calc(5, 2, '-') == 3

    def test_3(self):
        assert function.calc(6, 3, '*') == 18

    def test_4(self):
        assert function.calc(6, 3, '/') == 2

    def test_5(self):
        with pytest.raises(TypeError):
            assert function.calc(3, '+', 4)

    def test_6(self):
        with pytest.raises(TypeError):
            assert function.calc(3, 'adad', 4)
