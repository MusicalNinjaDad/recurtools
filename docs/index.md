# Welcome to recurtools

So many questions on StackExchange take the form "How do I ... with a nested ...?".
Here are some tools and helpers I developed to solve those kinds of problems

!!! danger "unstable interface"

    This is a 0.x.x version because I am not yet happy with the function naming. Expect the API to change.

Currently standard functionality is to traverse left-to-right as the collection would be output by `print()`

!!! warning "A note on strings"

    Handling of strings is not yet consistent. Sometimes they are separated into individual characters, and sometimes preserved as whole strings. This will be standardised by the v1.0.0 release and any further changes will be considered "breaking"

::: recurtools.nested

::: recurtools