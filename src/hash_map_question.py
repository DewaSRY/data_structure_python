""" 
"""

from typing import Mapping


def firstRecurring(array: list[int]):
    numMap: Mapping[int, bool] = {}
    for num in array:
        try:
            if numMap[num]:
                return num
        except Exception as e:
            numMap[num] = True

    return False
