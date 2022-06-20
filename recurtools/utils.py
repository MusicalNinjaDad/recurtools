from contextlib import contextmanager
from typing import Sequence, Sized

def flatten(seq):
    """
    Recursively flattens a sequence (including strings!) and returns all elements in order left to right.
    E.g.: [1,2,[3,4,[5],6],7,[8,9]] -> [1,2,3,4,5,6,7,8,9]
    """
    try:
        iterable = [x for x in seq]
    except TypeError:
        yield seq
    else:
        for item in iterable:
            if item is seq: #catch e.g. a single char string
                yield item
            else:
                yield from flatten(item)

def chainanything(*args, preservestrings=True, recursive=False):
    """
    Generator: yields the contents of a Sequence, or the given object if not a Sequence, one at a time
    
    preservestrings = False will lead to strings being yielded as individual characters. Default = True
    recursive = True will recursively flatten sequences. Default = False
    
    Note: preservestrings = False, recursive = False will only flatten strings which are not part of another Sequence.
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

def lenrecursive(seq):
    """
    Returns total summed length of all elements recursively.
    If no elements support len then return will be 0, no TypeError will be raised
    """
    def _len(x):
        try:
            return len(x)
        except TypeError: #no len
            return 0
    
    try:
        return _len(seq) + sum(lenrecursive(s) for s in seq if not isinstance(s, str))
    except TypeError: #not iterable
        return _len(seq)

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

def countrecursive(seq,val):
    """
    Returns total count of occurences of val in seq recursively.
    If no elements contain val then return will be 0
    """
    def _count(seq,val):
        count_ = 0
        for x in seq:
            if x == val:
                count_ += 1
        return count_
    
    return _count(flatten(seq),val)

def inrecursive(seq,val):
    """
    Searches seq recursively for val. Returns True if val found, False if val not found.
    If seq is not iterable tests seq == val . E.g. inrecursive(6,6) == True
    """
    def _in(seq, val):
        found = False
        for x in seq:
            found = (x == val)
            if found: break
        return found

    return _in(flatten(seq),val)

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
