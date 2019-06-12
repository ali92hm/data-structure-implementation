
class ArrayError(Exception):
    pass

class IndexOutOfBoundsError(Exception):
    pass


class Array():
    __data = list()
    size = 0
    capacity = 0

    def __init__(self, capacity=0):
        self.capacity = capacity
        self.clear()

    def add(self, element):
        if self.capacity == self.size:
            self.__resize()
        self.__data[self.size] = element
        self.size += 1

    def extend(self, array):
        pass

    def find(self, value):
        pass

    def remove(self, value):
        pass

    def reverse(self):
        pass

    def sort(self, sort_func, comparetor):
        pass

    def copy(self):
        pass

    def clear(self):
        self.size = 0
        self.__data = [0] * self.capacity

    def __getitem__(self, key):
        if key < 0 or key >= self.size:
            raise IndexOutOfBoundsError
        return self.__data[key]

    def __setitem__(self, key, value):
        if key < 0 or key >= self.size:
            raise IndexOutOfBoundsError
        self.__data[key] = value

    def __delattr__(self, key):
        pass

    def __len__(self):
        return self.size

    def __str__(self):
        array_string = '{'
        for key in range(len(self)):
            array_string += str(self[key]) + ('' if key + 1 == len(self) else ', ')
        array_string += '}'
        return array_string

    def __resize(self, expansion_factor = 2):
        if self.capacity == 0:
            self.capacity = 1
        else:
            self.capacity *= expansion_factor

        resizedArray = [0] * self.capacity
        for i in range(self.size):
            resizedArray[i] = self.__data[i]

        self.__data = resizedArray
        assert(len(self.__data), self.capacity)
