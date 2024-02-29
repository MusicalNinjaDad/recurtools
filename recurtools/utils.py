# noqa: D100

from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Generator, Iterable

stringlike = (str, bytes)

def flatten(nestediterable: Iterable, *, preserve: type | Iterable[type] | None = stringlike) -> Generator:
    """
    Recursively flattens a nested iterable and returns all elements in order left to right.

    Args:
    ----
    `nestediterable`: The nested iterable to flatten

    Keyword Args:
    ------------
    `preserve`: Optional type which will not be flattened. Default: `(str, bytes)`.  
    If you want to flatten strings then use `preserve=None`.


    !!! Note "bytes"
        `bytes` are flattened into individual `int` codes, unless `preserve` includes `bytes`.
        See [PEP467](https://peps.python.org/pep-0467/) for more background

    Examples:
    --------
    ```
    >>> [x for x in flatten([1,2,[3,4,[5],6],7,[8,9]])]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

    ```
    >>> [x for x in flatten([1,2,"abc",[3,4]], preserve = None)]
    [1, 2, 'a', 'b', 'c', 3, 4]
    ```

    ```
    >>> [x for x in flatten([1,2,"abc",[3,4]])]
    [1, 2, 'abc', 3, 4]
    ```
    """
    try:
        iter(nestediterable)
    except TypeError:
        yield nestediterable
    else:
        if preserve and isinstance(nestediterable, preserve):
            yield nestediterable
        else:
            for item in nestediterable:
                if item is nestediterable:  # catch e.g. a single char string
                    yield item
                else:
                    yield from flatten(item, preserve=preserve)


def starchain(
    *args: Any, preserve: type | Iterable[type] | None = stringlike, recursive: bool = True,  # noqa: ANN401
) -> Generator[Any]:
    """
    Generator: yields the contents of `args` one element at a time.
    
    Similar to itertools.chain but will accept non-iterable arguments and recurse into nested iterables.

    Args:
    ----
    `args`: one or more items to be chained.

    Keyword Args:
    ------------
    `preserve`: iterable types to be preserved as complete entities. Default:  Default: `(str, bytes)`.  
    If you want to yield individual characters from strings use `preserve = None`
    
    `recursive`: whether to recurse into nested iterables (`True`) , or yield them as a single entits (`False`).
    Default: `True`

    
    Examples:
    --------
    ```pycon
    >>> list(starchain([[1,2],[3,4]], 5))
    [1, 2, 3, 4, 5]
    ```
    
    !!! Note
        `preservestrings = None`, `recursive = False` will only flatten strings which are not part of another iterable.

        ```
        >>> list(starchain("abcd", preserve = None, recursive = False))
        ['a', 'b', 'c', 'd']

        >>> list(starchain(["ab", "cd"], preserve = None, recursive = False))
        ['ab', 'cd']
        ```
    """
    args = [*args]
    for arg in args:
        try:
            iter(arg)
        except TypeError:  # noqa: PERF203
            yield arg
        else:
            if preserve and isinstance(arg, preserve):
                yield arg
            elif recursive:
                yield from flatten(arg, preserve=preserve)
            else:
                yield from arg

def sumrecursive(seq):  # noqa: ANN001, ANN201
    """
    Returns total sum of all elements recursively.
    If no elements support sum then return will be 0, no TypeError will be raised
    """  # noqa: D205, D400, D415

    def _sum(seq):  # noqa: ANN001
        s = 0
        for x in seq:
            try:  # noqa: SIM105
                s = sum((s, x))
            except TypeError:  # noqa: PERF203
                pass
        return s

    return _sum(flatten(seq))


def countrecursive(collection, val):  # noqa: ANN001, ANN201
    """
    Returns total count of occurences of val in (nested) collection recursively.
    If no elements contain val then return will be 0
    """  # noqa: D205, D400, D415

    def _count(collection, val):  # noqa: ANN001
        count_ = 0
        for x in collection:
            if x == val:
                count_ += 1
        return count_

    return _count(flatten(collection, preserve=None), val)


def inrecursive(collection, val):  # noqa: ANN001, ANN201
    """
    Searches (nested) collection recursively for val. Returns True if val found, False if val not found.
    If collection is not iterable tests collection == val . E.g. inrecursive(6,6) == True
    """  # noqa: D205, D400, D415

    def _in(collection, val):  # noqa: ANN001
        found = False
        for x in collection:
            found = x == val
            if found:
                break
            else:  # could be a non-iterable container returned by flatten  # noqa: RET508
                try:  # noqa: SIM105
                    found = val in x
                except TypeError:
                    ...
                if found:
                    break
        return found

    return _in(flatten(collection), val)


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
            if s is not seq:  # single char strings etc.
                with ignoreException(NotFoundError), ignoreException(NoIndexError):
                    return tuple(flatten((i, indexrecursive(s, val))))
        raise NotFoundError

    try:
        with swapException(AttributeError, NoIndexError):
            return (seq.index(val),)
    except ValueError:  # not found but supports index, aasume also iterable
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
