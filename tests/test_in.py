
from .. import inrecursive

# https://stackoverflow.com/questions/72321903/deep-list-count-count-lists-within-lists

def test_in_ints():
    assert inrecursive([1, 2, [3, 2]],3) == True

def test_in_mixed():
    assert inrecursive([1,2,"bed",[7,'bob']], 'o') == True

def test_in_int():
    assert inrecursive(6,6) == True

def test_in_mixed_notfound():
    assert inrecursive([1,2,"bed",[7,'bob']], 5) == False