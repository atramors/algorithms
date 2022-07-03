# BINARY SEARCH

from typing import List, Union


random_list = [0.5, 1, 2.3, 3, 5, 7, 8.5, 9, 13, 15, 21, 64, 99]


def binary_search(array: List, value: int) -> Union[int, bool]:
    """searching value in the list"""
    # NB! for this algorithm array must be sorted

    min_element = 0
    max_element = len(array) - 1
    middle_element = (max_element + min_element) // 2
    while (array[middle_element] != value) and (min_element <= max_element):
        if value > array[middle_element]:
            min_element = middle_element + 1
        else:
            max_element = middle_element - 1
        middle_element = (max_element + min_element) // 2

    return middle_element if array[middle_element] == value else False
