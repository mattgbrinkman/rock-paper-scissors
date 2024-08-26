import unittest

# Assuming these are the imports needed
from main import determine_outcome, winning_combinations, losing_combinations

class Player:
    def __init__(self):
        self.move = ''
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.winner = False

#Rock = 1, Paper = 2, Scissors = 3
class TestDetermineOutcome(unittest.TestCase):
    
    def setUp(self):
        self.player1 = Player()
        self.player2 = Player()

    def test_tie(self):
        self.player1.move = 1
        self.player2.move = 1
        result = determine_outcome(self.player1, self.player2)
        self.assertEqual(result, "Tie")
        self.assertEqual(self.player1.ties, 1)
        self.assertEqual(self.player2.ties, 1)

    def test_rock_beats_scissors(self):
        self.player1.move = 1 #Rock
        self.player2.move = 3 #Scissors
        result = determine_outcome(self.player1, self.player2)
        self.assertEqual(result, "rock beats scissors")
        self.assertEqual(self.player1.wins, 1)
        self.assertEqual(self.player2.losses, 1)

    def scissors_beats_paper(self):
        self.player1.move = 3 #Scissors
        self.player2.move = 2 #Paper
        result = determine_outcome(self.player1, self.player2)
        self.assertEqual(result, "scissors beats paper")
        self.assertEqual(self.player1.wins, 1)
        self.assertEqual(self.player2.losses, 1)
    
    def paper_beats_rock(self):
        self.player1.move = 2 #Paper
        self.player2.move = 1 #Rock
        result = determine_outcome(self.player1, self.player2)
        self.assertEqual(result, "paper beats rock")
        self.assertEqual(self.player1.wins, 1)
        self.assertEqual(self.player2.losses, 1)

    def test_scissors_loses_to_rock(self):
        self.player1.move = 3 #Scissors
        self.player2.move = 1 #Rock
        result = determine_outcome(self.player1, self.player2)
        self.assertEqual(result, "scissors loses to rock")
        self.assertEqual(self.player1.losses, 1)
        self.assertEqual(self.player2.wins, 1)

    def test_paper_loses_to_scissors(self):
        self.player1.move = 2 #Paper
        self.player2.move = 3 #Scissors
        result = determine_outcome(self.player1, self.player2)
        self.assertEqual(result, "paper loses to scissors")
        self.assertEqual(self.player1.losses, 1)
        self.assertEqual(self.player2.wins, 1)

    def test_rock_loses_to_paper(self):
        self.player1.move = 1 #Rock
        self.player2.move = 2 #Paper
        result = determine_outcome(self.player1, self.player2)
        self.assertEqual(result, "rock loses to paper")
        self.assertEqual(self.player1.losses, 1)
        self.assertEqual(self.player2.wins, 1)

if __name__ == '__main__':
    unittest.main()