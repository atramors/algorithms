import unittest
from search.binary import binary_search
from search.linear import linear_search

from sorting.bubble import bubble_sort
from greedy.coin_change import greedy_coin_change_problem
from sorting.insertion import insertion_sort
from sorting.selection import selection_sort


class TestSortingAlgo(unittest.TestCase):

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


class TestGreedyAlgo(unittest.TestCase):

    def test_greedy(self):
        sample = {500: 0, 100: 3, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 0}
        result = greedy_coin_change_problem(500, 113)
        self.assertEqual(result, sample)


class TestSearchingAlgo(unittest.TestCase):

    def test_linear_search(self):
        result = linear_search([5, 2, 1, 6, 8, 3, 7, 4, 0, 9], 8)
        self.assertEqual(result, 4)

    def test_binary_search(self):
        result = binary_search([0.5, 1, 2.3, 3, 5, 7, 8.5, 9, 13, 15, 21, 64, 99], 7)
        self.assertEqual(result, 5)
