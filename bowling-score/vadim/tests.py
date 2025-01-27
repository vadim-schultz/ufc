from .implementation import get_score

def test_all_strikes():
    rolls = "X X X X X X X X X XXX"
    assert get_score(rolls) == 300

def test_all_spares():
    rolls = "5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5"
    assert get_score(rolls) == 150

def test_mixed_rolls():
    rolls = "9- 9- 9- 9- 9- 9- 9- 9- 9- 9-"
    assert get_score(rolls) == 90

def test_random_rolls():
    rolls = "X 7/ 9- X -8 8/ -6 X X X81"
    assert get_score(rolls) == 167

def test_tenth_frame_spare():
    rolls = "9- 9- 9- 9- 9- 9- 9- 9- 9- 9/5"
    assert get_score(rolls) == 95

def test_tenth_frame_strike():
    rolls = "9- 9- 9- 9- 9- 9- 9- 9- 9- X53"
    assert get_score(rolls) == 103