import pytest

a_string = "hello"
a_int = 1
a_float = 1.5
a_bool = False

def test_vars():
    assert type(a_string) == str
    assert type(a_int) == int
    assert type(a_float) == float
    assert type(a_bool) == bool
    