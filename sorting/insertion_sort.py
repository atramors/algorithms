# INSERTION SORT

from typing import List, Tuple


unsorted_list = [5, 2, 1, 6, 8, 3, 7, 4, 0, 9]


def insertion_sort(array: List) -> Tuple[List, int]:
    """Sorting arrays"""

    count_iterations = 0
    for i in range(len(array)):
        key_element = array[i]
        j = i - 1
        while j >= 0 and key_element < array[j]:
            array[j + 1] = array[j]
            j -= 1
            count_iterations += 1
        array[j + 1] = key_element

    return array, count_iterations


sorted_list, count_iterations = insertion_sort(unsorted_list)

print(f"Sorted list: {sorted_list}\n{count_iterations = }")
