from src.main import Calculator


def test_add():
    a = 3
    b = 2
    res = 5
    assert Calculator().add(a, b) == res
def test_sub():
    a = 3
    b = 2
    res = 1
    assert Calculator().sub(a, b) == res
def test_multi():
    a = 2
    b = 2
    res = 4
    assert Calculator().multi(a, b) == res
def test_div():
    a = 3
    b = 2
    res = 1.5
    assert Calculator().div(a, b) == res