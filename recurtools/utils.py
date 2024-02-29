# noqa: D100

from __future__ import annotations

from contextlib import contextmanager
from typing import Generator, Iterable

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


class Nonexistent:  # noqa: D101
    instance = None

    def __new__(cls):  # noqa: ANN204, D102
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __repr__(self) -> str:
        return "<Nonexistent>"

    def __str__(self) -> str:
        return "Nonexistent"
