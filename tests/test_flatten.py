from recurtools import flatten


def test_list():
    nested = [1,2,[3,4,[5],6],7,[8,9]]
    assert [x for x in flatten(nested)] == [1,2,3,4,5,6,7,8,9]  # noqa: C416

def test_tuple():
    nested = ((1,(2,),(3,4),5,(6,7,8)),9)
    assert [x for x in flatten(nested)] == [1,2,3,4,5,6,7,8,9]  # noqa: C416

def test_string():
    nested = ["abc", ["def,gh", "i,j"],["k",["l,m"]],"no"]
    assert "".join(flatten(nested)) == "abcdef,ghi,jkl,mno"

def test_nested_list_len1():
    nested = [1,[[2,3]]]
    assert [x for x in flatten(nested)] == [1,2,3]  # noqa: C416

def test_nested_list_len1_str():
    nested = [1,[[2,3,"a"]]]
    assert [x for x in flatten(nested)] == [1,2,3,"a"]  # noqa: C416

def test_set():
    nested = {1,(2,3),(4,(5,)),"ab"}
    flat = [x for x in flatten(nested)]  # noqa: C416
    for x in [1,2,3,4,5,"a","b"]:
        assert flat.count(x) == 1

def test_dict():
    nested = {
        1: (2,3),
        4: 5,
        (6,7): 8,
        9: 10,
    }
    assert [x for x in flatten(nested)] == [1,4,6,7,9]  # noqa: C416

def test_dict_values():
    nested = {
        1: (2,3),
        4: 5,
        (6,7): 8,
        9: 10,
    }
    assert [x for x in flatten(nested.values())] == [2,3,5,8,10]  # noqa: C416

def test_preservestrings():
    nested = ["ab",3,("cd","e")]
    assert [x for x in flatten(nested, preservestrings=True)] == ["ab",3,"cd","e"]  # noqa: C416

def test_dontflatten_str():
    nested = ["ab",3,("cd","e")]
    assert list(flatten(nested, dontflatten=str)) == ["ab",3,"cd","e"]
