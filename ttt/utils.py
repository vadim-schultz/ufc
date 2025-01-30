import typing as ty
import numpy as np
from dataclasses import dataclass


def schedule_from_players(players: ty.List[str]):
    np.random.seed(0)
    num_players = len(players)

    # players = [Player(name=name) for name in players]
    matches = []
    for i in range(10):
        # Shuffle players
        np.random.shuffle(players)

        round_x = np.split(np.array(players), 2)

        # Convert back to lists
        round_x = [x.tolist() for x in round_x]
        matches.append(round_x)

    # Convert to list of dictionary
    # matches = [dict(zip(players, match)) for match in matches]

    return matches
