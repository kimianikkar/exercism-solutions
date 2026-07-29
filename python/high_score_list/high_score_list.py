"""
Exercise: High Scores

Goal:
Create a class that manages a player's high scores.
Implement methods to:
- Return the highest score.
- Return the latest score.
- Return the top three highest scores.
"""


class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def personal_top_three(self):
        return sorted(self.scores, reverse=True)[:3]