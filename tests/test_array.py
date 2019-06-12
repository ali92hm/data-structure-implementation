import unittest
import random
from src import Array

def insertElements(array, number):
    for i in range(number):
        array.add(random.randint(0, 100))


class ArrayTestWithZeroCapacity(unittest.TestCase):
    def setUp(self):
        self.array = Array.Array()

    def test_capacity_should_be_zero(self):
        self.assertEqual(self.array.capacity, 0)

    def test_size_should_be_zero(self):
        self.assertEqual(len(self.array), 0)


    def test_adding_element_size_should_increase_size_and_capacity(self):
        self.array.add(4)
        self.assertEqual(self.array.size, 1)
        self.assertEqual(self.array.capacity, 2)

    #
    def test_delattr_should_remove_element(self):
        pass

    # Test for __len__
    def test_size_should_be_equals_to_len(self):
        self.assertEqual(len(self.array), self.array.size)
        insertElements(self.array, 15)
        self.assertEqual(len(self.array), self.array.size)

    # Test for __str__
    def test_srt_representation(self):
        self.assertEqual(str(self.array), '{}')
        self.array.add(4)
        self.assertEqual(str(self.array), '{4}')
        self.array.add(5)
        self.array.add(6)
        self.array.add(7)
        self.assertEqual(str(self.array), '{4, 5, 6, 7}')


class ArrayTestWithInitialCapacity(unittest.TestCase):
    __initial_capacity = 10
    def setUp(self):
        self.array = Array.Array(self.__initial_capacity)

    def test_capacity_should_be_initial_capacity(self):
        self.assertEqual(self.array.capacity, self.__initial_capacity)

    def test_size_should_be_zero(self):
        self.assertEqual(len(self.array), 0)

    def test_adding_element_size_should_increase_size_but_not_capacity(self):
        self.array.add(4)
        self.assertEqual(self.array.size, 1)
        self.assertEqual(self.array.capacity, self.__initial_capacity)
