from typing import Generic, TypeVar

T = TypeVar("T")


class Array(Generic[T]):
    def __init__(self, capacity: int = 0):
        pass

    def append(self, element: T) -> None:
        pass

    def extend(self, array: "Array[T]") -> None:
        pass

    def find(self, value: T) -> int:
        pass

    def remove(self, value: T) -> None:
        pass

    def reverse(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def __getitem__(self, key: int) -> T:
        pass

    def __setitem__(self, key: int, value: T) -> None:
        pass

    def __delitem__(self, key: int) -> None:
        pass

    def __len__(self) -> int:
        pass

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        return repr(self)

    # def __iter__(self):
    #     pass

    # def __next__(self):
    #     pass
