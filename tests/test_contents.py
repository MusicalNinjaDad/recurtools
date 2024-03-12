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

def test_flatten_preserveNone():  # noqa: N802
        nest=nested([1,2,"abc",[3,4]])
        assert list(nest.flatten(preserve = None)) == [1, 2, "a", "b", "c", 3, 4]