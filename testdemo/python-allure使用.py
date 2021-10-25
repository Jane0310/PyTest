import pytest

def test_success():
    assert True

def test_dailure():
    assert False

def test_skip():
    pytest.skip("for a reason!")

def test_broken():
    raise Exception("oops")

