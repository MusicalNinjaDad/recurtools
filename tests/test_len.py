from numpy import array

from recurtools import nested

# https://stackoverflow.com/questions/72321903/deep-list-count-count-lists-within-lists

def test_len_ints():
    assert len(nested([1, 2, [3, 4]])) == 4

def test_len_strs():
    assert len(nested(["a", "b", ["c", "d", ["e"]]])) == 5

def test_len_emptylists():
    assert len(nested([[[]]])) == 0

def test_len_docstring():
    assert len(nested(6)) == 1

def test_len_numpyarray():
    assert len(nested(array([[1,2],[3,4]]))) == 4

def test_len_countcollections():
    assert len(nested([1, 2, [3, 4]], countcontainers=True)) == 5

def test_len_singleint_countcollections():
    assert len(nested(6, True)) == 0  # noqa: FBT003
