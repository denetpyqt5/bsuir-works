from ppois.first.src.pyatnashki import Fives
import pytest


@pytest.mark.parametrize("matrix, expected", [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8], [3, 1]),
    ([1, 0, 2, 3, 4, 5, 6, 7, 8], [4, 1, 2]),
    ([1, 2, 0, 3, 4, 5, 6, 7, 8], [5, 2]),
    ([1, 2, 3, 0, 4, 5, 6, 7, 8], [1, 6, 4]),
    ([1, 2, 3, 4, 0, 5, 6, 7, 8], [2, 7, 4, 5]),
    ([1, 2, 3, 4, 5, 0, 6, 7, 8], [3, 8, 5]),
    ([1, 2, 3, 4, 5, 6, 0, 7, 8], [4, 7]),
    ([1, 2, 3, 4, 5, 6, 7, 0, 8], [5, 7, 8]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 0], [6, 8]),
])
def test_move(matrix, expected):
    g = Fives()
    g.current_matrix = matrix
    assert sorted(g._move()) == sorted(expected)

