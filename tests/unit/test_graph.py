import pytest

from data_structure_implementation import AdjacencyList, AdjacencyMatrix, Edge


class TestGraph:
    def build_graph(self, graph):
        graph.add_edge("A", "B")
        graph.add_edge("B", "C", directed=True)
        graph.add_edge("A", "C")
        graph.add_edge("A", "D", weight=2)
        graph.add_edge("A", "E", directed=True)

    def get_neighbors_assertions(self, graph):
        assert graph.get_neighbors("A") == [
            Edge("B", 1),
            Edge("C", 1),
            Edge("D", 2),
            Edge("E", 1),
        ]

        assert graph.get_neighbors("B") == [
            Edge("A", 1),
            Edge("C", 1),
        ]

        assert graph.get_neighbors("C") == [
            Edge("A", 1),
        ]

        assert graph.get_neighbors("D") == [
            Edge("A", 2),
        ]

        assert graph.get_neighbors("E") == []

        with pytest.raises(ValueError):
            graph.get_neighbors("Z")

    def test_adjacency_list(self):
        graph = AdjacencyList()
        self.build_graph(graph)
        assert sorted(graph.vertices) == ["A", "B", "C", "D", "E"]
        self.get_neighbors_assertions(graph)

    def test_adjacency_matrix(self):
        vertices = ["A", "B", "C", "D", "E"]
        graph = AdjacencyMatrix(vertices)
        self.build_graph(graph)
        assert sorted(graph.vertices) == vertices
        self.get_neighbors_assertions(graph)
