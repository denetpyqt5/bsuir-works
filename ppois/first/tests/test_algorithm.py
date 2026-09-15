from ppois.first.src.algorithm import  MarkovNormalAlgorithms
import pytest

@pytest.mark.parametrize(
    "state, rules, index, expected",
    [
        ("ABC", {"A": "B"}, 0, "BBC\n"),
        ("ABC", {"B": "C"}, 1, "ACC\n"),
        ("ABC", {"C": "A"}, 2, "ABA\n"),
    ],
)
def test_change(state, rules, index, expected):
    alg = MarkovNormalAlgorithms(state, **rules)
    info = alg._change(index)
    assert info == expected