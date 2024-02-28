# noqa: D100
from typing import Collection, Container

from recurtools.utils import countrecursive, flatten, inrecursive, lenrecursive


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
