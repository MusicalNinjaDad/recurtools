# noqa: D100
from contextlib import suppress
from typing import Any, Collection, Container

from recurtools.utils import countrecursive, flatten


class nested(Collection):  # noqa: N801
    """
    A `Collection` which supports recursive versions of `in`, `len` and offers a recursive `count`.

    Attributes:
    ----------
    `nestediterable`: the original nested content

    Examples:
    --------
    ```
    >>> numberlists = [[1, 2], [3, 4], [5, 6], [[7, 8], 9]]
    >>> nest = nested(numberlists)
    
    >>> nest.nestedcontainer
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
    def __init__(self, nestedcontainer: Container) -> None:
        self.nestedcontainer = nestedcontainer

    def __contains__(self, __other: Any) -> bool:  # noqa: ANN401
        def _in(collection, val):  # noqa: ANN001
            for x in collection:
                if x == val: return True  # noqa: E701
                with suppress(TypeError): # x not guaranteed to support __contains__
                    if val in x: return True  # noqa: E701
            return False

        return _in(flatten(self.nestedcontainer), __other)

    def __len__(self):  # noqa: ANN204
        return len(list(flatten(self.nestedcontainer)))

    def __iter__(self):  # noqa: ANN204
        return flatten(self.nestedcontainer)

    def count(self, __o):  # noqa: ANN001, ANN201, D102
        return countrecursive(self.nestedcontainer, __o)
