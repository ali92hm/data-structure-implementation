from data_structure_implementation.search import binary_search
from data_structure_implementation.errors import ValueNotFoundError

import pytest


class TestSearch:
    def test_binary_search_element_exist(self):
        arr = [-10, -5, -4, -4, 0, 3, 5, 10, 10, 150, 151, 152, 160, 700, 1200]

        assert binary_search(arr, 150) == 9
        assert binary_search(arr, 0) == 4
        assert binary_search(arr, 700) == 13
        assert binary_search(arr, -5) == 1
        assert binary_search(arr, -4) == 3
        assert binary_search(arr, 10) == 7
        with pytest.raises(ValueNotFoundError):
            binary_search(arr, 20)
