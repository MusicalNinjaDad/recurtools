# noqa: D100
from __future__ import annotations

from contextlib import suppress
from typing import Any, Collection, Container, Iterable

from recurtools.utils import flatten


class nested(Collection):  # noqa: N801
    """
    A `Collection` which supports recursive versions of `in`, `len` and offers a recursive `count` and `index`.

    Attributes:
    ----------
    contents: the original nested content

    Examples:
    --------
    ```
    >>> numberlists = [[1, 2], [3, 4], [5, 6], [[7, 8], 9]]
    >>> nest = nested(numberlists)
    
    >>> nest.contents
    [[1, 2], [3, 4], [5, 6], [[7, 8], 9]]

    >>> 5 in nest
    True

    >>> 10 in nest
    False

    >>> len(nest)
    9

    >>> [x for x in nest]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> list(nest)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> nest.count(5)
    1
    ```
    """
    def __init__(self, contents: Container) -> None:
        self.contents = contents


    def __contains__(self, __other: Any) -> bool:
        
        def _in(collection: Iterable, val: Any):
            for item in collection: # by using flatten in the call to _in, we are guaranteed an initial iterable
                if item == val: return True
                with suppress(TypeError): # item is not guaranteed to support __contains__
                    if val in item: return True
            return False

        return _in(flatten(self.contents), __other)


    def __len__(self):  # noqa: ANN204
        return len(list(flatten(self.contents)))

    def __iter__(self):  # noqa: ANN204
        return flatten(self.contents)

    def count(self, x: Any) -> int:
        """
        Return the number of times x occurs within the nested structure.

        Examples:
        --------
        ```
        >>> nest = nested([1, 2, [3, 2]])
        >>> nest.count(2)
        2
        >>> nest.count(4)
        0
        ```

        ```
        >>> nest = nested(["ab", "b", ["c", "db", ["e","bob"]]])
        >>> nest.count("b")
        5
        ```
        """
        return list(flatten(self.contents, preserve=None)).count(x)

    def index(self, x: Any) -> tuple[int]:
        """
        Return zero-based index in the nested structure of the first item whose value is equal to x. 
        
        Index is of the form a tuple with index at each level of the hierarchy.
        Raises a ValueError if there is no such item.

        Examples:
        --------
        ```
        >>> nest = nested([1, 2, [3, 2]])
        >>> nest.index(2)
        (1,)
        >>> nest.index(3)
        (2, 0)
        >>> nest.index(4)
        Traceback (most recent call last):
        ...
        ValueError: 4 is not in nest
        ```

        ```
        >>> nest = nested(["Foo",[1,"Bar"]])
        >>> nest.index("a")
        (1, 1, 1)
        ```
        """

        class NotFoundError(LookupError):
            pass
        class NoIndexError(LookupError):
            pass

        def _indexrecursive(seq, val):  # noqa: ANN001
            try:
                return (seq.index(val),)
            except AttributeError as a: # seq does not support index()
                raise NoIndexError from a
            except ValueError as v: # seq does support index() but val not found
                for i, s in enumerate(seq):
                    if s is not seq:  # single char strings etc.
                        with suppress(NotFoundError, NoIndexError):
                            return tuple(flatten((i, _indexrecursive(s, val))))
                raise NotFoundError from v
        try:
            return _indexrecursive(self.contents, x)
        except NotFoundError:
            raise ValueError (f"{x} is not in nest") from None  # noqa: EM102, TRY003