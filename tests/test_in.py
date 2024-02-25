
from collections.abc import Container

from recurtools import inrecursive

# https://stackoverflow.com/questions/72321903/deep-list-count-count-lists-within-lists

def test_in_ints():
    assert inrecursive([1, 2, [3, 2]],3) == True  # noqa: E712

def test_in_mixed():
    assert inrecursive([1,2,"bed",[7,"bob"]], "o") == True  # noqa: E712

def test_in_int():
    assert inrecursive(6,6) == True  # noqa: E712

def test_in_mixed_notfound():
    assert inrecursive([1,2,"bed",[7,"bob"]], 5) == False  # noqa: E712

def test_in_noniterablecontainer():
    class noniterablelist(Container):  # noqa: N801
        def __init__(self, contents) -> None:
            self.contents = contents
        def __contains__(self, __x: object) -> bool:
            return __x in self.contents

    input = noniterablelist([1,2,3,4])  # noqa: A001
    assert inrecursive(input, 3) == True  # noqa: E712