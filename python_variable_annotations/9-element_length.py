#!/usr/bin/env python3
'''
## 9. Let's Duck Type an Iterable Object
Annotate the below function's parameters and return values with the appropriate types.
```
def element_length(lst):
    return [(i, len(i)) for i in lst]
```
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Function that returns a list of tuples in a list
    '''
    return [(i, len(i)) for i in lst]
