from .. import chainanything

def test_splitstring():
    a = [1, 2, 3]
    b = "de"  # <-- not a (usual) list !
    c = 5     # <-- not a list !
    d = [4, 5, 23, 11, 5]
    e = ["dg", "kuku"]
    assert [x for x in chainanything(a,b,c,d,e,preservestrings=False)] == [1, 2, 3, "d","e", 5, 4, 5, 23, 11, 5, "dg", "kuku"]

def test_preservestring():
    # https://stackoverflow.com/questions/72288401/how-to-concat-lists-integers-and-strings-into-one-string/72288721#72288721
    a = [1, 2, 3]
    b = "de"  # <-- not a (usual) list !
    c = 5     # <-- not a list !
    d = [4, 5, 23, 11, 5]
    e = ["dg", "kuku"]
    assert [x for x in chainanything(a,b,c,d,e)] == [1, 2, 3, "de", 5, 4, 5, 23, 11, 5, "dg", "kuku"]

def test_flatten():
    a = [1, 2, 3]
    b = "de"  # <-- not a (usual) list !
    c = 5     # <-- not a list !
    d = [4, 5, 23, 11, 5]
    e = ["dg", "kuku"]
    assert [x for x in chainanything(a,b,c,d,e, recursive=True, preservestrings=False)] == [1, 2, 3, "d","e", 5, 4, 5, 23, 11, 5, "d","g", "k","u","k","u"]

def test_docstring():
    a = 'abc'
    b = ['ab','cd']
    assert [x for x in chainanything(a, preservestrings=False, recursive=False)] == ['a','b','c']
    assert [x for x in chainanything(b, preservestrings=False, recursive=False)] == ['ab','cd']

def test_join():
    a = [1, 2, 3]
    b = "de"  # <-- not a (usual) list !
    c = 5     # <-- not a list !
    d = [4, 5, 23, 11, 5]
    e = ["dg", "kuku"]
    assert ''.join(map(str,chainanything(a,b,c,d,e))) == "123de54523115dgkuku"