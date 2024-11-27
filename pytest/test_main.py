import pytest
from contextlib import nullcontext as does_not_raise

from src.main import Calculator

class Test_Calculator:

    @pytest.mark.parametrize(
            "a, b, res, expectation",
            [
                (3, 2.0, 5, does_not_raise()),
                (5, -3, 2, does_not_raise()),
                (5, "0", 5, pytest.raises(TypeError)),
            ]
    )
    def test_add(self, a, b, res, expectation):
        with expectation:
            assert Calculator().add(a, b) == res


    @pytest.mark.parametrize(
            "a, b, res, expectation",
            [
                (3, 2.0, 1, does_not_raise()),
                (5, -3, 8, does_not_raise()),
                (5, "0", 5, pytest.raises(TypeError)),
            ]
        )
    def test_sub(self, a, b, res, expectation):
        with expectation:
            assert Calculator().sub(a, b) == res
    

    @pytest.mark.parametrize(
            "a, b, res, expectation",
            [
                (3, 2.0, 6, does_not_raise()),
                (5, -3, -15, does_not_raise()),
                (4, "4", 5, pytest.raises(TypeError)),
            ]
        )
    def test_multi(self, a, b, res, expectation):
        with expectation:
            assert Calculator().multi(a, b) == res
    

    @pytest.mark.parametrize(
            "a, b, res, expectation",
            [
                (3, 2, 1.5, does_not_raise()),
                (6, -3, -2, does_not_raise()),
                (5, "1", 5, pytest.raises(TypeError)),
                (5, 0, 0, pytest.raises(ZeroDivisionError)),
            ]
    )
    def test_div(self, a, b, res, expectation):
        with expectation:
            assert Calculator().div(a, b) == res