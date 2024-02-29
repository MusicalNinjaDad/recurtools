from recurtools import nested

# https://stackoverflow.com/questions/72321903/deep-list-count-count-lists-within-lists

def test_count_ints():
    assert nested([1, 2, [3, 2]]).count(2) == 2

def test_count_strs():
    assert nested(["ab", "b", ["c", "db", ["e","bob"]]]).count("b") == 5
