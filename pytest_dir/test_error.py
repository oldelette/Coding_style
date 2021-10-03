import pytest

def func(x):
    if x==0:
        raise ValueError("value error!")
    else:
        pass


def test_mytest1():
    """
    try:
        func(0)
    except ValueError as error:
        print(error)
    """
    with pytest.raises(ValueError):
        func(0)

def test_mytest2():
    assert func(1) ==None


test_mytest1()


"""
def name_test(name):
    names=["Mike","Peter","Json"]
    if name not in names:
        raise ValueError("name does not exist.")
    print(name)


try:
    name_test("Gavin")
except ValueError as error:
    print(error)
"""
