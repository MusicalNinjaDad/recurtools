from .. import lenrecursive
from numpy import array

# https://stackoverflow.com/questions/72321903/deep-list-count-count-lists-within-lists

def test_len_ints():
    assert lenrecursive([1, 2, [3, 4]]) == 5

def test_len_strs():
    assert lenrecursive(["a", "b", ["c", "d", ["e"]]]) == 7

def test_len_emptylists():
    assert lenrecursive([[[]]]) == 2

def test_len_docstring():
    assert lenrecursive(6) == 0

def test_len_numpyarray():
    assert lenrecursive(array([[1,2],[3,4]])) == 6