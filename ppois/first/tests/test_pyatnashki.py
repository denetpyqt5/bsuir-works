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

import pytest
from ppois.first.src.pyatnashki import Fives


@pytest.mark.parametrize("start, tiles", [
    ([1, 2, 3, 4, 5, 6, 7, 0, 8], [8]),
    ([1, 2, 3, 4, 5, 6, 0, 7, 8], [7, 8]),
    ([1, 2, 3, 0, 5, 6, 4, 7, 8], [4, 7, 8]),
], ids=["one_move", "two_moves", "three_moves"])
def test_win_after_moves(start, tiles):
    g = Fives()
    g.current_matrix = start
    for tile in tiles:
        g.choose(tile)
    assert g.current_matrix == [1, 2, 3, 4, 5, 6, 7, 8, 0]