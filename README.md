# enveloop

[![PyPI version](https://badge.fury.io/py/enveloop.svg)](https://badge.fury.io/py/enveloop)
[![Build Status](https://travis-ci.com/arrrlo/enveloop.svg?branch=master)](https://travis-ci.com/arrrlo/enveloop)
![GitHub](https://img.shields.io/github/license/arrrlo/enveloop.svg?color=blue)
![GitHub last commit](https://img.shields.io/github/last-commit/arrrlo/enveloop.svg?color=blue)

Various utilities for handling loops, recursions, etc.

## Limit number of recursions

Let's say you wrote a recursive function and you want to limit number of recursions, just to be infinite loop free, or for any other reason.

```python
from enveloop import limit_recursion_to


# let's limit the number of recursion to 100

@limit_recursion_to(100)
def my_func(arg):
    ...
    my_func(arg)
    ...


# let's limit the number of recursion and after 
# the 10th recursion run a callback function.
# callback function takes exactly the same arguments
# as the recursion function.

@limit_recursion_to(10, lambda arg: ...)
def my_func(arg):
    ...
    my_func(arg)
    ...
``` 

## Changelog

### 0.1.0

#### Added:
- limit_recursion_to()
