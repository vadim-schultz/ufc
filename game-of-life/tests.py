import pytest

from example.implementation import evolve


@pytest.mark.parametrize(
    "initial_state, expected_state, wrapping",
    [
        # Test still life (block pattern)
        (
            [[1, 1],
             [1, 1]],
            [[1, 1],
             [1, 1]],
            False,
        ),
        # Test oscillating life (blinker pattern)
        (
            [[0, 1, 0],
             [0, 1, 0],
             [0, 1, 0]],
            [[0, 0, 0],
             [1, 1, 1],
             [0, 0, 0]],
            False,
        ),
        # Test glider pattern (wrapping grid)
        (
            [[0, 1, 0],
             [0, 0, 1],
             [1, 1, 1]],
            [[0, 0, 0],
             [1, 0, 1],
             [0, 1, 1]],
            True,
        ),
        # Test empty grid (all cells dead)
        (
            [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]],
            [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]],
            False,
        ),
    ],
)
def test_evolve(initial_state, expected_state, wrapping):
    assert evolve(initial_state) == expected_state


def test_large_grid():
    initial_state = [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    expected_state = [
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert evolve(initial_state) == expected_state


def test_custom_rules():
    initial_state = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0],
    ]
    expected_state = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]
    assert evolve(initial_state, wrapping=False, custom_rules={"birth": [2], "survival": [1, 2]}) == expected_state


def test_wrapping_behavior():
    initial_state = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1],
    ]
    expected_state = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert evolve(initial_state, wrapping=True) == expected_state
