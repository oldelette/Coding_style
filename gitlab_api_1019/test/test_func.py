import sys
sys.path.append("..")
from func import *
import pytest

def test_judge():
    status=judge("ls")
    assert status==True

def test_pylint():
    status = pylint("testt.py")
    assert status!=True

def test_flake8():
    status = flake8("testt.py")
    assert status!=True

def test_create():
    pass

