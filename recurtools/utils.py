from contextlib import contextmanager
from typing import Collection, Container, Sequence, Sized

def flatten(nestediterable, preservestrings = False):
    """
    Recursively flattens a nested iterable (including strings!) and returns all elements in order left to right.
    E.g.: [1,2,[3,4,[5],6],7,[8,9]] -> [1,2,3,4,5,6,7,8,9]

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

def chainanything(*args, preservestrings=True, recursive=False):
    """
    Generator: yields the contents of an iterable, or the given object if not a iterable, one at a time
    
    preservestrings = False will lead to strings being yielded as individual characters. Default = True
    recursive = True will recursively flatten container. Default = False
    
    Note: preservestrings = False, recursive = False will only flatten strings which are not part of another container.
    e.g.: 'abc' -> 'a','b','c' but ['ab','cd'] -> 'ab','cd'
    """
    args = [*args]
    for arg in args:
        if not isinstance(arg, Sequence):
            yield arg
        else:
            if preservestrings and isinstance(arg, str):
                yield arg
            elif recursive:
                yield from flatten(arg)
            else:
                yield from arg

def lenrecursive(container, countcontainers=False):
    """
    Returns total number of node elements in the (nested) container
    
    countcontainers=True: counts container collections and node elements.
    This is effectively recursively sum(len(c for c in container))
    Note:
        In this case if no elements support len the return will be 0, no TypeError will be raised
        lenrecursive(6) == 1
        lenrecursive(6, True) == 0
    """
    
    if countcontainers:
        def _len(x):
            try:
                return len(x)
            except TypeError: #no len
                return 0
        
        try:
            return _len(container) + sum(lenrecursive(c, countcontainers=True) for c in container if c is not container)
        except TypeError: #not iterable
            return _len(container)
    else:
        return len([x for x in flatten(container)])

def lenrecursiveshort(seq):
    return len(seq) + sum(lenrecursiveshort(s) for s in seq if isinstance(s,Sized) and not isinstance(s, str))

def sumrecursive(seq):
    """
    Returns total sum of all elements recursively.
    If no elements support sum then return will be 0, no TypeError will be raised
    """
    def _sum(seq):
        s = 0
        for x in seq:
            try:
                s = sum((s,x))
            except TypeError:
                pass
        return s
    
    return _sum(flatten(seq))

def countrecursive(collection,val):
    """
    Returns total count of occurences of val in (nested) collection recursively.
    If no elements contain val then return will be 0
    """
    def _count(collection,val):
        count_ = 0
        for x in collection:
            if x == val:
                count_ += 1
        return count_
    
    return _count(flatten(collection),val)

def inrecursive(collection,val):
    """
    Searches (nested) collection recursively for val. Returns True if val found, False if val not found.
    If collection is not iterable tests collection == val . E.g. inrecursive(6,6) == True
    """
    def _in(collection, val):
        found = False
        for x in collection:
            found = (x == val)
            if found: break
            else: #could be a non-iterable container returned by flatten
                try:
                    found = val in x
                except TypeError:
                    ...
                if found: break
        return found

    return _in(flatten(collection),val)

class NotFoundError(LookupError):
    pass

class NoIndexError(LookupError):
    pass

@contextmanager
def ignoreException(ExceptionType):
    try:
        yield
    except ExceptionType:
        pass

@contextmanager
def swapException(OriginalException, NewException):
    try:
        yield
    except OriginalException:
        raise NewException

def indexrecursive(seq, val):

    def _lookinchildren(seq, val):
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

class Nonexistent(object):
    instance = None
    
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def __repr__(self) -> str:
        return "<Nonexistent>"

    def __str__(self) -> str:
        return "Nonexistent"

class nested(Collection):
    def __init__(self, nestedcontainer: Container) -> None:
        self.nestedcontainer = nestedcontainer
    
    def __contains__(self, __o: object) -> bool:
        return inrecursive(self.nestedcontainer, __o)

    def __len__(self):
        return lenrecursive(self.nestedcontainer)

    def __iter__(self):
        return flatten(self.nestedcontainer)

    def count(self, __o):
        return countrecursive(self.nestedcontainer, __o)