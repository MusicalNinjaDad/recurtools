from recurtools import nested

def test_storescollection():
    input = [1,2,[3,4,[5],6],7,[8,9]]
    nest = nested(input)
    assert nest.nestedcontainer == input

def test_len():
    input = [1,2,[3,4,[5],6],7,[8,9]]
    nest = nested(input)
    assert len(nest) == 9

def test_in():
    input = [1,2,[3,4,[5],6],7,[8,9]]
    nest = nested(input)
    assert 4 in nest
    assert 0 not in nest

def test_count():
    input = [1,2,[3,2,[5],6],7,[2,9]]
    nest = nested(input)
    assert nest.count(2) == 3

def test_iterate():
    input = [1,2,[3,4,[5],6],7,[8,9]]
    nest = nested(input)
    out = [x for x in nest]
    assert out == [1,2,3,4,5,6,7,8,9]