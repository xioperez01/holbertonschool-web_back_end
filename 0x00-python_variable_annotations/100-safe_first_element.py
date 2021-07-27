
#!/usr/bin/env python3
"""python module"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''any and none'''
    if lst:
        return lst[0]
    else:
        return None
