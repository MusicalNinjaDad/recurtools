from pytest import raises  # noqa: PT013

from recurtools import indexrecursive
from recurtools.utils import NotFoundError

# https://stackoverflow.com/questions/72321903/deep-list-count-count-lists-within-lists

def test_index_toplevel():
    assert indexrecursive([1, 2, [3, 2]],2) == (1,)

def test_index_int():
    assert indexrecursive([1, 2, [3, 2]],3) == (2,0)

def test_index_notfound():
    with raises(NotFoundError):
        indexrecursive([1, 2, [3, 2]],4)

def test_index_later():
    assert indexrecursive([1, 2, [3, 2],[[2,3],[5,5,3,4]]],4) == (3,1,3)

def test_string():
    assert indexrecursive("FooBar","B") == (3,)
    assert indexrecursive(["Foo",[1,"Bar"]],"a") == (1,1,1)

def test_set():
    assert indexrecursive([1,2,{3,4},[3,4]],4) == (3,1)
