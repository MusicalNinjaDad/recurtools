
from collections.abc import Container

from recurtools import nested

# https://stackoverflow.com/questions/72321903/deep-list-count-count-lists-within-lists

def test_in_ints():
    assert 3 in nested([1, 2, [3, 2]])

def test_in_mixed():
    assert "o" in nested([1,2,"bed",[7,"bob"]])

def test_in_int():
    assert 6 in nested(6)

def test_in_mixed_notfound():
    assert 5 not in nested([1,2,"bed",[7,"bob"]])

def test_in_noniterablecontainer():
    class noniterablelist(Container):  # noqa: N801
        def __init__(self, contents) -> None:
            self.contents = contents
        def __contains__(self, __x: object) -> bool:
            return __x in self.contents

    input = noniterablelist([1,2,3,4])  # noqa: A001
    assert 3 in nested(input)
