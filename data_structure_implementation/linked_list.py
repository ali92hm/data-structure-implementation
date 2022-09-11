from typing import Generic, TypeVar

T = TypeVar("T")


class LinkedListNode(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.next = None


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self._length = 0
        node = LinkedListNode(None)
        self._head = node
        self._tail = node

    def append(self, value: T) -> None:
        return None

    def append_left(self, value: T) -> None:
        pass

    def remove(self, node: LinkedListNode[T]) -> None:
        pass

    def peek_head(self) -> LinkedListNode[T]:
        pass

    def peek_tail(self) -> LinkedListNode[T]:
        pass

    def pop_head(self) -> LinkedListNode[T]:
        pass

    def pop_tail(self) -> LinkedListNode[T]:
        pass

    def __len__(self) -> int:
        return self._length

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        return repr(self)

    # def __iter__(self):
    #     pass

    # def __next__(self):
    #     pass
