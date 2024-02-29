from numpy import array

from recurtools import sumrecursive

# https://stackoverflow.com/questions/72321903/deep-list-count-count-lists-within-lists

def test_sum_ints():
    assert sumrecursive([1, 2, [3, 4]]) == 10

def test_sum_strs():
    assert sumrecursive(["a", "b", ["c", "d", ["e"]]]) == 0

def test_sum_emptylists():
    assert sumrecursive([[[]]]) == 0

def test_sum_docstring():
    assert sumrecursive(6) == 6

def test_sum_numpyarray():
    assert sumrecursive(array([[1,2],[3,4]])) == 10

def test_sum_mixed():
    assert sumrecursive([1,2.5,[4,"foo"],(5,(0.5,5))]) == 18
