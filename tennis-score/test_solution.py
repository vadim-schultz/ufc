import pytest

from florian.implementation import TennisGame


@pytest.fixture
def game():
    return TennisGame(players=["player1", "player2"])


def test_initial_score(game):
    assert game.get_score() == "Love-All"


def test_same_scores(game):
    game.add_point("player1")
    game.add_point("player2")
    assert game.get_score() == "Fifteen-All"

    game.add_point("player1")
    game.add_point("player2")
    assert game.get_score() == "Thirty-All"

    # Deuce case
    game.add_point("player1")
    game.add_point("player2")
    assert game.get_score() == "Deuce"


def test_simple_scores(game):
    # Player 1 scores points
    game.add_point("player1")
    assert game.get_score() == "Fifteen-Love"

    game.add_point("player1")
    assert game.get_score() == "Thirty-Love"

    game.add_point("player1")
    assert game.get_score() == "Forty-Love"


def test_opponent_scores(game):
    # Player 2 scores points
    game.add_point("player2")
    assert game.get_score() == "Love-Fifteen"

    game.add_point("player2")
    assert game.get_score() == "Love-Thirty"

    game.add_point("player2")
    assert game.get_score() == "Love-Forty"


def test_alternating_scores(game):
    game.add_point("player1")
    assert game.get_score() == "Fifteen-Love"

    game.add_point("player2")
    assert game.get_score() == "Fifteen-All"

    game.add_point("player1")
    assert game.get_score() == "Thirty-Fifteen"

    game.add_point("player2")
    assert game.get_score() == "Thirty-All"

    game.add_point("player1")
    assert game.get_score() == "Forty-Thirty"

    game.add_point("player2")
    assert game.get_score() == "Deuce"


def test_deuce_and_advantage(game):
    # Get to deuce
    for _ in range(3):
        game.add_point("player1")
        game.add_point("player2")

    assert game.get_score() == "Deuce"

    game.add_point("player1")
    assert game.get_score() == "Advantage player1"

    game.add_point("player2")
    assert game.get_score() == "Deuce"

    game.add_point("player2")
    assert game.get_score() == "Advantage player2"

    game.add_point("player1")
    assert game.get_score() == "Deuce"


def test_game_win_from_advantage(game):
    # Reach deuce first
    for _ in range(3):
        game.add_point("player1")
        game.add_point("player2")

    # Advantage and win for player 1
    game.add_point("player1")
    assert game.get_score() == "Advantage player1"

    game.add_point("player1")
    assert game.get_score() == "Game player1"


def test_game_win_without_deuce(game):
    # Straight win by player 1
    for _ in range(4):
        game.add_point("player1")

    assert game.get_score() == "Game player1"

    # Reset for player 2 win test
    game = TennisGame(["player1", "player2"])
    for _ in range(4):
        game.add_point("player2")

    assert game.get_score() == "Game player2"


def test_back_and_forth_advantage_win(game):
    # Get to deuce
    for _ in range(3):
        game.add_point("player1")
        game.add_point("player2")

    # Advantage back and forth
    game.add_point("player1")
    assert game.get_score() == "Advantage player1"

    game.add_point("player2")
    assert game.get_score() == "Deuce"

    game.add_point("player2")
    assert game.get_score() == "Advantage player2"

    game.add_point("player2")
    assert game.get_score() == "Game player2"
