from typing import List

from .graph import Graph
from .errors import ValueNotFoundError


def binary_search(arr: List[int], element: int) -> int:

    def _search(arr: List[int], element: int, low: int, high: int) -> int:
        if low > high:
            raise ValueNotFoundError(f'Element {element} was not found in array')

        mid_index = low + (high - low) // 2
        mid_element = arr[mid_index]
        if element == mid_element:
            return mid_index
        elif element > mid_element:
            return _search(arr, element, mid_index + 1, high)
        else:
            return _search(arr, element, low, mid_index - 1)

    return _search(arr, element, 0, len(arr) - 1)


def breadth_first_search(graph: Graph, start: str, end: str) -> List[str]:
    pass


def depth_first_search(graph: Graph, start: str, end: str) -> List[str]:
    pass


def find_rotation_index() -> None:
    pass
