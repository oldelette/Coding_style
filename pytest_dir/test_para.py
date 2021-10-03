import pytest

def add(x,y):
    return x+y

@pytest.mark.parametrize(
    "x,y,expected",
    [
        (1,1,2),
        (2,2,4),
        (10,10,20)
    ]
)

def test_add(x,y,expected):
    assert add(x,y) == expected


"""
def test1():
    assert 2 == add(1,1)

def test2():
    assert 1 != add(1,1)
"""
