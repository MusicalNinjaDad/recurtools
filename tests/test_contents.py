import pytest  # noqa: F401

from recurtools import nested


def test_list_nest():
    nest = nested([
        [1,2],
        [3,4],
        ["abc","def"],
    ])
    assert list(nest) == [1,2,3,4,"abc","def"]

def test_flatten_default():
    nest = nested([
        [1,2],
        [3,4],
        ["abc","def"],
    ])
    assert list(nest.flatten()) == [1,2,3,4,"abc","def"]