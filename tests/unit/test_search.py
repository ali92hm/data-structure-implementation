import pytest

from data_structure_implementation.errors import ValueNotFoundError
from data_structure_implementation.graph import AdjacencyList
from data_structure_implementation.search import (
    binary_search,
    breadth_first_search,
    depth_first_search,
)


class TestSearch:
    def test_binary_search(self):
        arr = [-10, -5, -4, -4, 0, 3, 5, 10, 10, 150, 151, 152, 160, 700, 1200]

        assert binary_search(arr, 150) == 9
        assert binary_search(arr, 0) == 4
        assert binary_search(arr, 700) == 13
        assert binary_search(arr, -5) == 1
        assert binary_search(arr, -4) == 3
        assert binary_search(arr, 10) == 7
        with pytest.raises(ValueNotFoundError):
            binary_search(arr, 20)

    @pytest.fixture
    def graph(self):
        g = AdjacencyList()

        # First component
        g.add_edge("A", "B", directed=True)
        g.add_edge("A", "C", directed=True)
        g.add_edge("B", "C", directed=False)
        g.add_edge("B", "D", directed=True)
        g.add_edge("B", "E", directed=True)
        g.add_edge("C", "F", directed=True)
        g.add_edge("E", "F", directed=True)

        # Second component
        g.add_edge("T", "U", directed=True)
        g.add_edge("U", "W", directed=True)
        g.add_edge("W", "T", directed=True)

        return g

    def test_breadth_first_search(self, graph):
        assert breadth_first_search(graph, "A", "E") == ["A", "B", "E"]
        assert breadth_first_search(graph, "C", "D") == ["C", "B", "D"]
        assert breadth_first_search(graph, "C", "F") == ["C", "F"]
        assert breadth_first_search(graph, "T", "W") == ["T", "U", "W"]

        with pytest.raises(ValueNotFoundError):
            assert breadth_first_search(graph, "C", "A")

        with pytest.raises(ValueNotFoundError):
            assert breadth_first_search(graph, "A", "T")

    def test_depth_first_search_1(self, graph):
        """
        The path returned by DFS depends on the order of edge insertion in the
        graph generator
        """

        assert depth_first_search(graph, "A", "E") == ["A", "B", "C", "F", "D", "E"]

        assert depth_first_search(graph, "C", "D") == ["C", "B", "D"]
        assert depth_first_search(graph, "C", "F") == ["C", "B", "D", "E", "F"]
        assert depth_first_search(graph, "T", "W") == ["T", "U", "W"]

        with pytest.raises(ValueNotFoundError):
            assert depth_first_search(graph, "C", "A")

        with pytest.raises(ValueNotFoundError):
            assert depth_first_search(graph, "A", "T")
