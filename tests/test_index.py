import pytest

from recurtools import nested
from recurtools.utils import NotFoundError

# https://stackoverflow.com/questions/72321903/deep-list-count-count-lists-within-lists

def test_index_toplevel():
    assert nested([1, 2, [3, 2]]).index(2) == (1,)

def test_index_int():
    assert nested([1, 2, [3, 2]]).index(3) == (2,0)

@pytest.mark.xfail()
def test_index_notfound():
    with pytest.raises(NotFoundError):
        nested([1, 2, [3, 2]]).index(4)

def test_index_later():
    assert nested([1, 2, [3, 2],[[2,3],[5,5,3,4]]]).index(4) == (3,1,3)

def test_string():
    assert nested("FooBar").index("B") == (3,)
    assert nested(["Foo",[1,"Bar"]]).index("a") == (1,1,1)

def test_set():
    assert nested([1,2,{3,4},[3,4]]).index(4) == (3,1)
