import pytest

from recurtools import nested


def test_list_nest():
    nest = nested([
        [1,2],
        [3,4],
        ["abc","def"],
    ])
    assert list(nest) == [1,2,3,4,"abc","def"]

@pytest.mark.xfail(reason="Not Implemented")
def test_flatten_default():
    nest = nested([
        [1,2],
        [3,4],
        ["abc","def"],
    ])
    assert list(nest.flatten()) == [1,2,3,4,"abc","def"]