# SELECTION SORT

from typing import List, Tuple


unsorted_list = [5, 2, 1, 6, 8, 3, 7, 4, 0, 9]


def selection_sort(array: List) -> Tuple[List, int]:
    """Sorting arrays"""

    count_iterations = 0
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array) - 1):
            if array[min_index] > array[j]:
                min_index = j
                count_iterations += 1
        array[i], array[min_index] = array[min_index], array[i]

    return array, count_iterations


sorted_list, count_iterations = selection_sort(unsorted_list)

print(f"Sorted list: {sorted_list}\n{count_iterations = }")
