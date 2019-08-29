class DLinkedNode():
    def __init__(self, value):
        self.value = value
        self._prev = None
        self._next = None

class DLinkedList():
    def __init__(self):
        self._length = 0
        self._head = None
        self._tail = None

    def append(self, node):
        node._next = None
        self._length += 1

        if self._head:
            self._head._next = node
            node._prev = self._head

        self._head = node

        if not self._tail:
            self._tail = node

    def append_left(self, node):
        node._prev = None
        self._length += 1

        if self._tail:
            self._tail._prev = node
            node._next = self._tail

        self._tail = node

        if not self._head:
            self._head = node

    def move(self, node):
        if node == self._head:
            return

        self.remove(node)
        self.append(node)

    def move_left(self, node):
        if node == self._tail:
            return

        self.remove(node)
        self.append_left(node)

    def remove(self, node):
        if not self._head or not self._tail:
            raise Exception()

        self._length -= 1
        if self._tail == self._head:
            self._tail = None
            self._head = None
        elif node == self._tail:
            self._tail = node._next
            self._tail._prev = None
        elif node == self._head:
            self._head = node._prev
            self._head._next = None
        else:
            node._next._prev = node._prev
            node._prev._next = node._next

    def peek(self):
        if not self._head or not self._tail:
            raise Exception()
        return self._head

    def peek_left(self):
        if not self._head or not self._tail:
            raise Exception()
        return self._tail

    def pop(self):
        last = self._head
        self.remove(last)
        return last

    def pop_left(self):
        first = self._tail
        self.remove(first)
        return first

    def __len__(self):
        return self._length

    def __repr__(self):
        count = 1
        string = '['
        for node in self:
            string += str((node._prev.value if node._prev else None, node.value, node._next.value if node._next else None)) + ('' if count == len(self) else ', ')
            count += 1
        string += ']'
        return string

    def __str__(self):
        return repr(self)

    def __iter__(self):
        current = self._tail
        while current:
            yield current
            current = current._next

    # def __iter__(self):
    #     self.__current = self._tail
    #     return self

    # def __next__(self):
    #     if self.__current:
    #         current = self.__current
    #         self.__current = self.__current._next
    #         return current
    #     else:
    #         raise StopIteration

if __name__ == "__main__":
    dl = DLinkedList()
    print(dl)
    a = DLinkedNode(10)
    dl.append(a)
    print(dl)

    print(dl.pop_left().value)
    print(dl)

    # b = DLinkedNode(11)
    # dl.append(b)
    # print(dl)

    # c = DLinkedNode(12)
    # dl.append(c)
    # print(dl)

    # d = DLinkedNode(13)
    # dl.append(d)
    # print(dl)

    # hash_pop = hash(dl.pop_left())
    # print(hash_pop, hash(a))
    # print(dl)

