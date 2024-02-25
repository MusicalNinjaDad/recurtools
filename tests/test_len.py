from numpy import array

from recurtools import lenrecursive

# https://stackoverflow.com/questions/72321903/deep-list-count-count-lists-within-lists

def test_len_ints():
    assert lenrecursive([1, 2, [3, 4]]) == 4

def test_len_strs():
    assert lenrecursive(["a", "b", ["c", "d", ["e"]]]) == 5

def test_len_emptylists():
    assert lenrecursive([[[]]]) == 0

def test_len_docstring():
    assert lenrecursive(6) == 1

def test_len_numpyarray():
    assert lenrecursive(array([[1,2],[3,4]])) == 4

def test_len_countcollections():
    assert lenrecursive([1, 2, [3, 4]], countcontainers=True) == 5

def test_len_singleint_countcollections():
    assert lenrecursive(6, True) == 0
