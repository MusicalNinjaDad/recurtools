# recurtools

So many questions on StackExchange take the form "How do I ... with a nested list?".
Here are some tools and helpers I developed to solve those kinds of problems

**WARNING** This is a 0.x.x version because I am not yet happy with the function naming. Expect the API to change.

Currently standard functionality is to traverse left-to-right as the collection would be output by `print()`

## Getting Started

Installation `pip install recurtools`

### flatten

A generator which will flatten any iterable collection recursively.

```python
from recurtools import flatten
input = [1,2,[3,4,[5],6],7,[8,9]]
assert [x for x in flatten(input)] == [1,2,3,4,5,6,7,8,9]
```

### nested

A `Container` which implements `lenrecursive`, `countrecursive`, `inrecursive` and `flatten` for `len()`, `.count()`, `in` and `for x in`

```python
from recurtools import nested
input = [1,2,[3,4,[5],6],7,[8,9]]
nest = nested(input)

assert len(nest) == 9
assert 4 in nest
assert 0 not in nest

out = [x for x in nest]
assert out == [1,2,3,4,5,6,7,8,9]

nest2 = nested([1,2,[3,2,[5],6],7,[2,9]])
assert nest2.count(2) == 3
```

### lenrecursive, sumrecursive, countrecursive, inrecursive

Recursive versions of `len`, `sum`, `count`, `in` and `index`.

Generally these will return a 0 or `None` value rather than raising an `TypeError` or `ValueError` as their nonrecursive brethren do.
`indexrecursive` is an exception and will raise a specific `NotFoundError`.

They can also cope with situations where some elements in the nested collection are summable / have a length etc. and others do not.

```python
from recurtools import lenrecursive
assert lenrecursive([1, 2, [3, 4]]) == 4
assert lenrecursive([1, 2, [3, 4]], countcontainers=True) == 5
```

```python
from recurtools import sumrecursive
assert sumrecursive([1, 2, [3, 4]]) == 10
assert sumrecursive([1,2.5,[4,"foo"],(5,(0.5,5))]) == 18
```

```python
from recurtools import countrecursive
assert countrecursive([1, 2, [3, 2]],2) == 2
assert countrecursive(["ab", "b", ["c", "db", ["e","bob"]]],'b') == 5
```

```python
from recurtools import inrecursive
assert inrecursive([1, 2, [3, 2]],3) == True
```

```python
from recurtools import indexrecursive
assert indexrecursive([1, 2, [3, 2]],2) == (1,)
assert indexrecursive([1, 2, [3, 2]],3) == (2,0)
assert indexrecursive(["Foo",[1,"Bar"]],"a") == (1,1,1)

with raises(NotFoundError):
        indexrecursive([1, 2, [3, 2]],4)
```

### chainanything

A generator that chains (m)anything(s).

```python
from recurtools import chainanything
a = [1, 2, 3]
b = "de"
c = 5     
d = [4, 5, 23, 11, 5]
e = ["dg", "kuku"]
assert [x for x in chainanything(a,b,c,d,e)] == [1, 2, 3, "de", 5, 4, 5, 23, 11, 5, "dg", "kuku"]
assert ''.join(map(str,chainanything(a,b,c,d,e))) == "123de54523115dgkuku"
```

preservestrings = False will lead to strings being yielded as individual characters. Default = `True`
recursive = True will recursively flatten container. Default = `False` (Warning: This may change in v1.0.0)

Note: preservestrings = False, recursive = False will only flatten strings which are not part of another container.
e.g.: 'abc' -> 'a','b','c' but ['ab','cd'] -> 'ab','cd'

```python
a = [1, 2, 3]
b = "de"
c = 5
d = [4, 5, 23, 11, 5]
e = ["dg", "kuku"]
assert [x for x in chainanything(a,b,c,d,e, recursive=False, preservestrings=False)] == [1, 2, 3, "d","e", 5, 4, 5, 23, 11, 5, "dg", "kuku"]
assert [x for x in chainanything(a,b,c,d,e, recursive=True, preservestrings=False)] == [1, 2, 3, "d","e", 5, 4, 5, 23, 11, 5, "d","g", "k","u","k","u"]
```
