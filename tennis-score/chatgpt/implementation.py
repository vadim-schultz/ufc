class TennisGame:
    def __init__(self):
        self.scores = { "player1": 0, "player2": 0 }

    def add_point(self, player):
        # Increment score for the player
        if player in self.scores:
            self.scores[player] += 1

    def get_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        p1_score = self.scores["player1"]
        p2_score = self.scores["player2"]

        # Check if a player has won
        if p1_score >= 4 or p2_score >= 4:
            score_diff = p1_score - p2_score
            if score_diff >= 2:
                return "Game player1"
            elif score_diff <= -2:
                return "Game player2"
            elif score_diff == 1:
                return "Advantage player1"
            elif score_diff == -1:
                return "Advantage player2"
            else:
                return "Deuce"

        # Standard scoring within first three points
        if p1_score == p2_score:
            return f"{score_names[p1_score]}-All" if p1_score < 3 else "Deuce"
        else:
            return f"{score_names[p1_score]}-{score_names[p2_score]}"
