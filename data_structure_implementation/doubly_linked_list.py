from typing import Generic, TypeVar

T = TypeVar("T")


class DoublyLinkedListNode(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self._length = 0
        node = DoublyLinkedListNode(None)
        self._head = node
        self._tail = node

    def append(self, value: T) -> None:
        return None

    def append_left(self, value: T) -> None:
        pass

    def remove(self, node: DoublyLinkedListNode[T]) -> None:
        pass

    def peek_head(self) -> DoublyLinkedListNode[T]:
        pass

    def peek_tail(self) -> DoublyLinkedListNode[T]:
        pass

    def pop_head(self) -> DoublyLinkedListNode[T]:
        pass

    def pop_tail(self) -> DoublyLinkedListNode[T]:
        pass

    def move_to_head(self, node: DoublyLinkedListNode[T]) -> None:
        pass

    def move_to_tail(self, node: DoublyLinkedListNode[T]) -> None:
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


# if __name__ == '__main__':
#     d = DoublyLinkedListNode(10)
#     print(d.value)
