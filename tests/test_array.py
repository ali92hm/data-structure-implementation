import unittest
from src.Array import Array
from src.Array import IndexOutOfBoundsError
from src.Array import ValueNotFoundError

def insertElements(array, number):
    for i in range(number):
        array.add(i)


class ArrayTestWithZeroCapacity(unittest.TestCase):
    def setUp(self):
        self.array = Array()

    # Tests constructor
    def test_capacity_should_be_zero(self):
        self.assertEqual(self.array.capacity, 0)

    # Test constructor
    def test_size_should_be_zero(self):
        self.assertEqual(len(self.array), 0)

    # Tests add
    def test_adding_elements_should_increase_size_and_capacity(self):
        # Adding first element
        self.array.add(1)
        self.assertEqual(self.array.size, 1)
        self.assertEqual(self.array.capacity, 1)

        # Adding second element, capacity should stay the same
        self.array.add(2)
        self.assertEqual(self.array.size, 2)
        self.assertEqual(self.array.capacity, 2)

        # Adding third element, capacity should double
        self.array.add(3)
        self.assertEqual(self.array.size, 3)
        self.assertEqual(self.array.capacity, 4)

    # Tests add
    def test_adding_many_elements_should_increase_size_and_capacity(self):
        number_of_elements = 68
        insertElements(self.array, number_of_elements)
        self.assertEqual(self.array.size, number_of_elements)
        self.assertEqual(self.array.capacity, 128)

    # Test extend
    def test_extend(self):
        pass

    # Test find
    def test_find(self):
        pass

    def test_indexOf_value_exists_should_return_index(self):
        value = 10
        self.array.add(value)
        key = self.array.indexOf(value)
        self.assertEqual(key, 0)

    def test_indexOf_two_value_exist_should_return_first_index(self):
        insertElements(self.array, 20)
        value = 10
        index = 4
        self.array[index] = value
        key = self.array.indexOf(value)
        self.assertEqual(key, index)

    def test_indexOf_value_does_not_exist_should_raise_ValueNotFoundError(self):
        insertElements(self.array, 20)
        with self.assertRaises(ValueNotFoundError):
            self.array.indexOf(100)

    # Test for __getitem__
    def test_can_get_an_item_using_brackets(self):
        value = 10
        self.array.add(value)
        self.assertEqual(self.array[0], value)

        value = 13
        self.array.add(value)
        self.assertEqual(self.array[1], value)

    # Test for __getitem__
    def test_access_empty_array_should_raise_exception(self):
        with self.assertRaises(IndexOutOfBoundsError):
            self.array[0]

    # Test for __getitem__
    def test_access_out_of_bounds_should_raise_exception(self):
        insertElements(self.array, 10)

        with self.assertRaises(IndexOutOfBoundsError):
            self.array[20]

    # Test for __getitem__
    def test_access_negative_index_should_raise_exception(self):
        insertElements(self.array, 10)

        with self.assertRaises(IndexOutOfBoundsError):
            self.array[-11]

    # Test for __setitem__
    def test_can_set_an_item_using_brackets(self):
        insertElements(self.array, 10)

        index = 1
        value = 10
        self.array[index] = value
        self.assertEqual(self.array[index], value)

        index = 4
        value = 30
        self.array[index] = value
        self.assertEqual(self.array[index], value)

    # Test for __setitem__
    def test_assignment_empty_array_should_raise_exception(self):
        with self.assertRaises(IndexOutOfBoundsError):
            self.array[0] = 10

    # Test for __setitem__
    def test_assignment_out_of_bounds_should_raise_exception(self):
        self.array.add(10)
        with self.assertRaises(IndexOutOfBoundsError):
            self.array[1] = 1

    # Test for __setitem__
    def test_assignment_negative_index_should_raise_exception(self):
        insertElements(self.array, 10)

        with self.assertRaises(IndexOutOfBoundsError):
            self.array[-11] = 1

    # Test for __delattr__
    def test_can_delete_item(self):
        self.array.add(10)
        del self.array[0]
        self.assertEqual(len(self.array), 0)

    # Test for __delattr__
    def test_delete_empty_array_should_raise_exception(self):
        pass

    # Test for __delattr__
    def test_delete_out_of_bounds_should_raise_exception(self):
        pass

    # Test for __delattr__
    def test_delete_negative_index_should_raise_exception(self):
        pass

    # Test for __len__
    def test_size_should_be_equals_to_len(self):
        number_of_elements = 68
        self.assertEqual(len(self.array), self.array.size)
        insertElements(self.array, number_of_elements)
        self.assertEqual(len(self.array), self.array.size)
        self.assertEqual(len(self.array), number_of_elements)

    # Test for __repr__
    def test_repr_representation(self):
        self.assertEqual(repr(self.array), '[]')
        self.array.add(4)
        self.assertEqual(repr(self.array), '[4]')
        self.array.add(5)
        self.array.add(6)
        self.array.add(7)
        self.assertEqual(repr(self.array), '[4, 5, 6, 7]')

    # Test for __str__
    def test_str_representation_should_be_same_as_repr(self):
        insertElements(self.array, 34)
        self.assertEqual(repr(self.array), str(self.array))


class ArrayTestWithInitialCapacity(unittest.TestCase):
    __initial_capacity = 10
    def setUp(self):
        self.array = Array(self.__initial_capacity)

    def test_capacity_should_be_initial_capacity(self):
        self.assertEqual(self.array.capacity, self.__initial_capacity)

    def test_size_should_be_zero(self):
        self.assertEqual(len(self.array), 0)

    def test_adding_element_size_should_increase_size_but_not_capacity(self):
        self.array.add(4)
        self.assertEqual(self.array.size, 1)
        self.assertEqual(self.array.capacity, self.__initial_capacity)
