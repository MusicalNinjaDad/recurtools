from recurtools.utils import Nonexistent


def test_instantiation():
    exists = Nonexistent()
    assert isinstance(exists, Nonexistent)

def test_singleton():
    exists1 = Nonexistent()
    exists2 = Nonexistent()
    assert exists1 is exists2

def test_repr():
    exists = Nonexistent()
    assert exists.__repr__() == "<Nonexistent>"
    assert str(exists) == "Nonexistent"
