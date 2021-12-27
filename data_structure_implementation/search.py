from collections import OrderedDict, defaultdict, deque
from typing import Deque, Dict, List

from .errors import ValueNotFoundError
from .graph import Edge, Graph


def binary_search(arr: List[int], element: int) -> int:
    def _search(arr: List[int], element: int, low: int, high: int) -> int:
        if low > high:
            raise ValueNotFoundError(f"Element {element} was not found in array")

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
    queue: Deque[Edge] = deque()
    path: Dict[str, List[str]] = defaultdict(list)

    queue.append(Edge(start, 0))
    path[start] = list([start])

    while queue:
        node = queue.popleft()
        if node.name == end:
            return path[end]

        for neighbor in graph.get_neighbors(node.name):
            if neighbor.name not in path:
                path[neighbor.name] = list(path[node.name] + [neighbor.name])
                queue.append(neighbor)

    raise ValueNotFoundError(f"Could not find a path from {start} to {end}")


def depth_first_search(graph: Graph, start: str, end: str) -> List[str]:
    def _depth_first_search(
        graph: Graph, start: str, end: str, visited: Dict[str, bool]
    ) -> List[str]:
        visited[start] = True
        if start == end:
            return list(visited.keys())

        path: List[str] = list()
        for neighbor in graph.get_neighbors(start):
            if neighbor.name not in visited:
                path.extend(_depth_first_search(graph, neighbor.name, end, visited))

        return path

    path = _depth_first_search(graph, start, end, OrderedDict())
    if not path:
        raise ValueNotFoundError(f"Could not find a path from {start} to {end}")

    return path


def find_rotation_index() -> None:
    pass
