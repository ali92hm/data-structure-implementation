
class ArrayError(Exception):
    pass

class IndexOutOfBoundsError(ArrayError):
    pass

class ValueNotFoundError(ArrayError):
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
        key = self.indexOf(value)
        return self[key]

    def indexOf(self, value):
        for i in range(len(self)):
            if value == self[i]:
                return i
        else:
            raise ValueNotFoundError

    def remove(self, value):
        key = self.indexOf(value)
        del self[key]

    def reverse(self):
        pass

    def clear(self):
        self.size = 0
        self.__data = [None] * self.capacity

    def __getitem__(self, key):
        if key < 0 or key >= self.size:
            raise IndexOutOfBoundsError

        return self.__data[key]

    def __setitem__(self, key, value):
        if key < 0 or key >= self.size:
            raise IndexOutOfBoundsError

        self.__data[key] = value

    def __delitem__(self, key):
        if key < 0 or key >= self.size:
            raise IndexOutOfBoundsError

        for i in range(key, len(self) - 1):
            self[i] = self[i + 1]

        self[len(self) - 1] = None
        self.size -= 1

    def __len__(self):
        return self.size

    def __repr__(self):
        array_string = '['
        for key in range(len(self)):
            array_string += str(self[key]) + ('' if key + 1 == len(self) else ', ')
        array_string += ']'
        return array_string

    def __str__(self):
        return repr(self)

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __resize(self, expansion_factor = 2):
        if self.capacity == 0:
            self.capacity = 1
        else:
            self.capacity *= expansion_factor

        resizedArray = [None] * self.capacity
        for i in range(self.size):
            resizedArray[i] = self.__data[i]

        self.__data = resizedArray
        assert(len(self.__data), self.capacity)
