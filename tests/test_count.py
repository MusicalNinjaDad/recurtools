from recurtools import countrecursive

# https://stackoverflow.com/questions/72321903/deep-list-count-count-lists-within-lists

def test_count_ints():
    assert countrecursive([1, 2, [3, 2]],2) == 2  # noqa: PLR2004

def test_count_strs():
    assert countrecursive(["ab", "b", ["c", "db", ["e","bob"]]],"b") == 5  # noqa: PLR2004
