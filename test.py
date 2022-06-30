import unittest

from sorting.bubble_sort import bubble_sort
from greedy.greedy_algo import greedy_algorithm
from sorting.insertion_sort import insertion_sort
from sorting.selection_sort import selection_sort


class TestAlgo(unittest.TestCase):

    def test_bubble(self):
        sample = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 19)
        result = bubble_sort([5, 2, 1, 6, 8, 3, 7, 4, 0, 9])
        self.assertEqual(result, sample)

    def test_selection_sorting(self):
        sample = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
        result = selection_sort([5, 2, 1, 6, 8, 3, 7, 4, 0, 9])
        self.assertEqual(result, sample)

    def test_insertion_sorting(self):
        sample = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 19)
        result = insertion_sort([5, 2, 1, 6, 8, 3, 7, 4, 0, 9])
        self.assertEqual(result, sample)

    def test_greedy(self):
        sample = {500: 0, 100: 3, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 0}
        result = greedy_algorithm(500, 113)
        self.assertEqual(result, sample)
