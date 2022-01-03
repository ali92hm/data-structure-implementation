from collections import defaultdict, namedtuple
from typing import Dict, List, Set

Edge = namedtuple("Edge", ["name", "weight"])


class Graph:
    def add_edge(
        self, from_node: str, to_node: str, weight: int = 1, directed: bool = False
    ) -> None:
        pass

    @property
    def vertices(self) -> List[str]:
        pass

    def get_neighbors(self, node: str) -> List[Edge]:
        pass


class AdjacencyMatrix(Graph):
    def __init__(self, vertices: List[str]):
        self._vertices: List[str] = vertices
        self._index_map: Dict[str, int] = dict()
        self._graph: List[List[int]] = [[]] * len(vertices)

        for index, value in enumerate(vertices):
            self._index_map[value] = index
            self._graph[index] = [0] * len(vertices)

    def add_edge(
        self, from_node: str, to_node: str, weight: int = 1, directed: bool = False
    ) -> None:
        if from_node not in self._index_map or to_node not in self._index_map:
            raise ValueError("Node not in graph")

        from_index = self._index_map[from_node]
        to_index = self._index_map[to_node]

        self._graph[from_index][to_index] = weight
        if not directed:
            self._graph[to_index][from_index] = weight

    @property
    def vertices(self) -> List[str]:
        return self._vertices

    def get_neighbors(self, node: str) -> List[Edge]:
        if node not in self._index_map:
            raise ValueError("Node not in graph")

        from_index = self._index_map[node]
        neighbors: List[Edge] = []
        for index, wight in enumerate(self._graph[from_index]):
            if wight != 0:
                neighbors.append(Edge(self._vertices[index], wight))

        return neighbors


class AdjacencyList(Graph):
    def __init__(self) -> None:
        self._vertices: Set[str] = set()
        self._edges: Dict[str, List[Edge]] = defaultdict(list)

    def add_edge(
        self, from_node: str, to_node: str, weight: int = 1, directed: bool = False
    ) -> None:
        self._vertices.add(from_node)
        self._vertices.add(to_node)

        self._edges[from_node].append(Edge(to_node, weight))

        if not directed:
            self._edges[to_node].append(Edge(from_node, weight))

    @property
    def vertices(self) -> List[str]:
        return list(self._vertices)

    def get_neighbors(self, node: str) -> List[Edge]:
        if node not in self._vertices:
            raise ValueError("Node not in graph")

        return self._edges[node]
