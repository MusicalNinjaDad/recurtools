
from typing import Container
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

def test_in_noniterablecontainer():
    class noniterablelist(Container):
        def __init__(self, contents) -> None:
            self.contents = contents
        def __contains__(self, __x: object) -> bool:
            return __x in self.contents
    
    input = noniterablelist([1,2,3,4])
    assert inrecursive(input, 3) == True