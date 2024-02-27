from recurtools import starchain


def test_splitstring():
    a = [1, 2, 3]
    b = "de"
    c = 5
    d = [4, 5, 23, 11, 5]
    e = ["dg", "kuku"]
    assert [x for x in starchain(a,b,c,d,e, recursive=False, preserve=None)] == [1, 2, 3, "d","e", 5, 4, 5, 23, 11, 5, "dg", "kuku"]  # noqa: C416, E501

def test_preservestring():
    # https://stackoverflow.com/questions/72288401/how-to-concat-lists-integers-and-strings-into-one-string/72288721#72288721
    a = [1, 2, 3]
    b = "de"
    c = 5
    d = [4, 5, 23, 11, 5]
    e = ["dg", "kuku"]
    assert [x for x in starchain(a,b,c,d,e)] == [1, 2, 3, "de", 5, 4, 5, 23, 11, 5, "dg", "kuku"]  # noqa: C416

def test_flatten():
    a = [1, 2, 3]
    b = "de"
    c = 5
    d = [4, 5, 23, 11, 5]
    e = ["dg", "kuku"]
    assert [x for x in starchain(a,b,c,d,e, recursive=True, preserve=None)] == [1, 2, 3, "d","e", 5, 4, 5, 23, 11, 5, "d","g", "k","u","k","u"]  # noqa: C416, E501

def test_docstring():
    a = "abc"
    b = ["ab","cd"]
    assert [x for x in starchain(a, preserve=None, recursive=False)] == ["a","b","c"]  # noqa: C416
    assert [x for x in starchain(b, preserve=None, recursive=False)] == ["ab","cd"]  # noqa: C416

def test_join():
    a = [1, 2, 3]
    b = "de"
    c = 5
    d = [4, 5, 23, 11, 5]
    e = ["dg", "kuku"]
    assert "".join(map(str,starchain(a,b,c,d,e))) == "123de54523115dgkuku"
