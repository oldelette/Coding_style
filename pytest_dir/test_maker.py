import pytest
import os
import tempfile
from time import sleep

"""
@pytest.mark.slow
def test_super_slow_test():
    sleep(3)

@pytest.mark.quick
def test_something_quick():
    pass
"""

@pytest.mark.g1
def test_func1():
    pass

@pytest.mark.g2
def test_func2():
    pass

@pytest.mark.g1
def test_func3():
    pass

@pytest.mark.g2
def test_func4():
    pass

@pytest.mark.g1
def test_func5():
    pass

"""
@pytest.fixture
def cleandir():
    old_cwd = os.getcwd()
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)
    yield
    os.chdir(old_cwd)
    shutil.rmtree(newpath)
"""
