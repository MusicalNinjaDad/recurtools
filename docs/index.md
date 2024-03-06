# About

A simple library to support working with recursively nested objects.

Primarily built around the [nested class](#nested) which offers `in`, `len`, `index()` and `count()` functionality.  
Additionally, the [flatten() function](#flatten) provides the ability to configure behaviour for strings etc.

!!! Tip "A note on strings in nested objects"

    When iterating through a nested object, string-like elements `(str, bytes)` will be returned in their original blocks, not as individual characters.  
    When calculating `len`, `index`, `count` and `__contains__`; individual characters are considered.
    
    A future version will aim to provide a similar interface to the `preserve` keyword argument in flatten.

## Quick reference - nested

Full details under [Reference - class nested](reference.md#recurtools.nested.nested)

``` mermaid
classDiagram
    direction RL
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
    handler: python
    options:
      members: false
      show_root_heading: false
      show_root_toc_entry: false