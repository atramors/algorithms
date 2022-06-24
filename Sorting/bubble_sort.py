# BUBBLE SORT ALGORITHM

from typing import List, Tuple


unsorted_list = [5, 2, 1, 6, 8, 3, 7, 4, 0, 9]


def bubble_sort(array: List) -> Tuple[List, int]:
    """Sorting arrays"""

    count_iterations = 0
    state = True
    while state:
        state = False

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                state = True
                array[i], array[i + 1] = array[i + 1], array[i]
                count_iterations += 1
    return array, count_iterations


sorted_list, count_iterations = bubble_sort(unsorted_list)

print(f"Sorted list: {sorted_list}\n{count_iterations = }")
