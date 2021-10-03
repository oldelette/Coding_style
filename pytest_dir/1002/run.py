import pytest

if __name__=='__main__':
    pytest.main(["--cov=./","--cov-report=html","--cov-config=.coveragerc"])
