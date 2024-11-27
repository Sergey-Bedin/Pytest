import pytest
from src.main import Calculator

class Test_Calculator:

    @pytest.mark.parametrize(
            "a, b, res",
            [
                (3, 2, 5),
                (5, -3, 2)
            ]
    )
    def test_add(self, a, b, res):
        assert Calculator().add(a, b) == res


    @pytest.mark.parametrize(
                "a, b, res",
                [
                    (3, 2, 1),
                    (5, -3, 8)
                ]
        )
    def test_sub(self, a, b, res):
        assert Calculator().sub(a, b) == res
    

    @pytest.mark.parametrize(
            "a, b, res",
            [
                (3, 2, 6),
                (5, -3, -15)
            ]
    )
    def test_multi(self, a, b, res):
        assert Calculator().multi(a, b) == res
    
    @pytest.mark.parametrize(
            "a, b, res",
            [
                (3, 2, 1.5),
                (6, -3, -2)
            ]
    )
    def test_div(self, a, b, res):
        assert Calculator().div(a, b) == res