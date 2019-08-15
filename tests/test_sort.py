import unittest
from src.Sort import quick_sort as sort

class TestSort(unittest.TestCase):

    def test_sort_array_None(self):
        arr = None
        self.assertEqual(sort(arr), None)

    def test_sort_array_empty(self):
        arr = []
        sorted_arr = sorted(arr)
        self.assertEqual(sort(arr), sorted_arr)

    def test_sort_array_one_element(self):
        arr = [4]
        sorted_arr = sorted(arr)
        self.assertEqual(sort(arr), sorted_arr)

    def test_sort_array_odd_length(self):
        arr = [4, 1, 2, 5, 3]
        sorted_arr = sorted(arr)
        self.assertEqual(sort(arr), sorted_arr)

    def test_sort_array_even_length(self):
        arr = [4, 1, 2, 5, 3, 6]
        sorted_arr = sorted(arr)
        self.assertEqual(sort(arr), sorted_arr)
