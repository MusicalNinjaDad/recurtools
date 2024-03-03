from recurtools import nested


def test_preservestrings():
    nest = nested([
        [1,2],
        [3,4],
        ["abc","def"],
    ])
    assert list(nest) == [1,2,3,4,"abc","def"]