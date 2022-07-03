# LINEAR SEARCH

from typing import List, Union


random_list = [5, 2, 1, 6, 8, 3, 7, 4, 0, 9]


def linear_search(array: List, value: int) -> Union[int, bool]:
    """searching value in the list"""

    for i in range(len(array)):
        if array[i] == value:
            return i

    return False
