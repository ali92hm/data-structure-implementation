from collections import namedtuple
from DLinkedList import DLinkedList
from DLinkedList import DLinkedNode

NodeData = namedtuple('NodeData', ['key', 'val'])

NodeData = namedtuple('NodeData', ['key', 'val'])


class LRUCache:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise Exception(
                'Cannot instantiate with negative or zero capacity')

        self._capacity = capacity
        self._list = DLinkedList()
        self._map = dict()

    def get(self, key) -> int:
        if key not in self._map:
            return -1

        element = self._map[key]
        self._list.move(element)
        return element.value.val

    def put(self, key, value) -> None:
        data = NodeData(key, value)
        if key in self._map:
            element = self._map[key]
            element.value = data
            self._list.move(element)
            return

        node = DLinkedNode(data)
        self._list.append(node)
        self._map[key] = node

        if len(self._list) > self._capacity:
            element = self._list.pop_left()
            del self._map[element.value.key]
