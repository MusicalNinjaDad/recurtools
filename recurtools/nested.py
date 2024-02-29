# noqa: D100
from typing import Collection, Container

from recurtools.utils import countrecursive, flatten, inrecursive


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

    def __contains__(self, __o: object) -> bool:  # noqa: D105
        return inrecursive(self.nestedcontainer, __o)

    def __len__(self):  # noqa: ANN204, D105
        return len(list(flatten(self.nestedcontainer)))

    def __iter__(self):  # noqa: ANN204, D105
        return flatten(self.nestedcontainer)

    def count(self, __o):  # noqa: ANN001, ANN201, D102
        return countrecursive(self.nestedcontainer, __o)
