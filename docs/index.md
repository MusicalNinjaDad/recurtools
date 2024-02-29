# recurtools

A simple library to support working with recursively nested objects.

Primarily built around the [nested class](#nested) which offers `in`, `len`, `index()` and `count()` functionality.  
Additionally, a [flatten() function](#flatten) is provided via `recurtools.utils`.

!!! Tip "A note on strings in nested objects"

    When iterating through a nested object, string-like elements `(str, bytes)` will be returned in their original blocks, not as individual characters.  
    When calculating `len`, `index`, `count` and `__contains__`; individual characters are considered.
    
    A future version will aim to provide a similar interface to the `preserve` keyword argument in flatten.

## Usage

```
from recurtools import nested
```

```
from recurtools import flatten
```

## Class Diagram

``` mermaid
classDiagram
    direction LR
    nested <|.. Collection: implements
    class nested{
        contents
        __contains__()
        __iter__()
        __len__()
        count()
        index()
    }
    class Collection["collections.abc.Collection"]
```



::: recurtools.nested.nested

::: recurtools.utils.flatten