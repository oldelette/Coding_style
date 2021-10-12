"""pytest_example"""
import sys

from src.func import cau

sys.path.append(".")


def test_add():
    """test_function"""
    num1 = cau(1, 2, 3)
    num2 = cau(2, 3, 2)
    num3 = cau(5, 3, 4)
    assert num1 == 5
    assert num2 == 1
    assert num3 == 12
