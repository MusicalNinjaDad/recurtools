from recurtools import flatten


def test_list():
    input = [1,2,[3,4,[5],6],7,[8,9]]  # noqa: A001
    assert [x for x in flatten(input)] == [1,2,3,4,5,6,7,8,9]  # noqa: C416

def test_tuple():
    input = ((1,(2,),(3,4),5,(6,7,8)),9)  # noqa: A001
    assert [x for x in flatten(input)] == [1,2,3,4,5,6,7,8,9]  # noqa: C416

def test_string():
    input = ["abc", ["def,gh", "i,j"],["k",["l,m"]],"no"]  # noqa: A001
    assert "".join(flatten(input)) == "abcdef,ghi,jkl,mno"

def test_nested_list_len1():
    input = [1,[[2,3]]]  # noqa: A001
    assert [x for x in flatten(input)] == [1,2,3]  # noqa: C416

def test_nested_list_len1_str():
    input = [1,[[2,3,"a"]]]  # noqa: A001
    assert [x for x in flatten(input)] == [1,2,3,"a"]  # noqa: C416

def test_set():
    input = {1,(2,3),(4,(5,)),"ab"}  # noqa: A001
    flat = [x for x in flatten(input)]  # noqa: C416
    for x in [1,2,3,4,5,"a","b"]:
        assert flat.count(x) == 1

def test_dict():
    input = {  # noqa: A001
        1: (2,3),
        4: 5,
        (6,7): 8,
        9: 10,
    }
    assert [x for x in flatten(input)] == [1,4,6,7,9]  # noqa: C416

def test_dict_values():
    input = {  # noqa: A001
        1: (2,3),
        4: 5,
        (6,7): 8,
        9: 10,
    }
    assert [x for x in flatten(input.values())] == [2,3,5,8,10]  # noqa: C416

def test_preservestrings():
    input = ["ab",3,("cd","e")]  # noqa: A001
    assert [x for x in flatten(input, preservestrings=True)] == ["ab",3,"cd","e"]  # noqa: C416
