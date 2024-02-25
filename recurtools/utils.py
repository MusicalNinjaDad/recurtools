from collections.abc import Collection, Container, Sequence, Sized  # noqa: D100
from contextlib import contextmanager


def flatten(nestediterable, preservestrings = False):  # noqa: ANN001, ANN201, FBT002
    """
    Recursively flattens a nested iterable (including strings!) and returns all elements in order left to right.

    Example:
    -------
    ```
    >>> [x for x in flatten([1,2,[3,4,[5],6],7,[8,9]])]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    ```

    preservestrings = True: will not flatten strings to individual characters
    """
    try:
        iter(nestediterable)
    except TypeError:
        yield nestediterable
    else:
        if preservestrings and isinstance(nestediterable, (str, bytes)):
                yield nestediterable
        else:
            for item in nestediterable:
                if item is nestediterable: #catch e.g. a single char string
                    yield item
                else:
                    yield from flatten(item, preservestrings)

def chainanything(*args, preservestrings=True, recursive=False):  # noqa: ANN001, ANN002, ANN201
    """
    Generator: yields the contents of an iterable, or the given object if not a iterable, one at a time

    preservestrings = False will lead to strings being yielded as individual characters. Default = True
    recursive = True will recursively flatten container. Default = False

    Note: preservestrings = False, recursive = False will only flatten strings which are not part of another container.
    e.g.: 'abc' -> 'a','b','c' but ['ab','cd'] -> 'ab','cd'
    """  # noqa: D400, D415
    args = [*args]
    for arg in args:
        if not isinstance(arg, Sequence):
            yield arg
        else:  # noqa: PLR5501
            if preservestrings and isinstance(arg, str):
                yield arg
            elif recursive:
                yield from flatten(arg)
            else:
                yield from arg

def lenrecursive(container, countcontainers=False):  # noqa: ANN001, ANN201, FBT002
    """
    Returns total number of node elements in the (nested) container

    countcontainers=True: counts container collections and node elements.
    This is effectively recursively sum(len(c for c in container))

    Note:
    ----
        In this case if no elements support len the return will be 0, no TypeError will be raised
        lenrecursive(6) == 1
        lenrecursive(6, True) == 0

    """  # noqa: D400, D415
    if countcontainers:
        def _len(x):  # noqa: ANN001
            try:
                return len(x)
            except TypeError: #no len
                return 0

        try:
            return _len(container) + sum(lenrecursive(c, countcontainers=True) for c in container if c is not container)
        except TypeError: #not iterable
            return _len(container)
    else:
        return len([x for x in flatten(container)])  # noqa: C416

def lenrecursiveshort(seq):  # noqa: ANN001, ANN201, D103
    return len(seq) + sum(lenrecursiveshort(s) for s in seq if isinstance(s,Sized) and not isinstance(s, str))

def sumrecursive(seq):  # noqa: ANN001, ANN201
    """
    Returns total sum of all elements recursively.
    If no elements support sum then return will be 0, no TypeError will be raised
    """  # noqa: D205, D400, D415
    def _sum(seq):  # noqa: ANN001
        s = 0
        for x in seq:
            try:  # noqa: SIM105
                s = sum((s,x))
            except TypeError:  # noqa: PERF203
                pass
        return s

    return _sum(flatten(seq))

def countrecursive(collection,val):  # noqa: ANN001, ANN201
    """
    Returns total count of occurences of val in (nested) collection recursively.
    If no elements contain val then return will be 0
    """  # noqa: D205, D400, D415
    def _count(collection,val):  # noqa: ANN001
        count_ = 0
        for x in collection:
            if x == val:
                count_ += 1
        return count_

    return _count(flatten(collection),val)

def inrecursive(collection,val):  # noqa: ANN001, ANN201
    """
    Searches (nested) collection recursively for val. Returns True if val found, False if val not found.
    If collection is not iterable tests collection == val . E.g. inrecursive(6,6) == True
    """  # noqa: D205, D400, D415
    def _in(collection, val):  # noqa: ANN001
        found = False
        for x in collection:
            found = (x == val)
            if found: break  # noqa: E701
            else: #could be a non-iterable container returned by flatten  # noqa: RET508
                try:  # noqa: SIM105
                    found = val in x
                except TypeError:
                    ...
                if found: break  # noqa: E701
        return found

    return _in(flatten(collection),val)

class NotFoundError(LookupError):  # noqa: D101
    pass

class NoIndexError(LookupError):  # noqa: D101
    pass

@contextmanager
def ignoreException(ExceptionType):  # noqa: ANN001, ANN201, D103, N802, N803
    try:  # noqa: SIM105
        yield
    except ExceptionType:
        pass

@contextmanager
def swapException(OriginalException, NewException):  # noqa: ANN001, ANN201, D103, N802, N803
    try:
        yield
    except OriginalException:
        raise NewException  # noqa: B904

def indexrecursive(seq, val):  # noqa: ANN001, ANN201, D103

    def _lookinchildren(seq, val):  # noqa: ANN001
        for i, s in enumerate(seq):
            if s is not seq: #single char strings etc.
                with ignoreException(NotFoundError), ignoreException(NoIndexError):
                    return tuple(flatten((i, indexrecursive(s, val))))
        raise NotFoundError

    try:
        with swapException(AttributeError, NoIndexError):
            return (seq.index(val),)
    except ValueError: #not found but supports index, aasume also iterable
        return _lookinchildren(seq, val)

class Nonexistent:  # noqa: D101
    instance = None

    def __new__(cls):  # noqa: ANN204, D102
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __repr__(self) -> str:  # noqa: D105
        return "<Nonexistent>"

    def __str__(self) -> str:  # noqa: D105
        return "Nonexistent"

class nested(Collection):  # noqa: D101, N801
    def __init__(self, nestedcontainer: Container) -> None:  # noqa: D107
        self.nestedcontainer = nestedcontainer

    def __contains__(self, __o: object) -> bool:  # noqa: D105
        return inrecursive(self.nestedcontainer, __o)

    def __len__(self):  # noqa: ANN204, D105
        return lenrecursive(self.nestedcontainer)

    def __iter__(self):  # noqa: ANN204, D105
        return flatten(self.nestedcontainer)

    def count(self, __o):  # noqa: ANN001, ANN201, D102
        return countrecursive(self.nestedcontainer, __o)
