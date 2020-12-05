import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.ace = Card('diamonds', 1)
        self.card2 = Card('diamonds', 5)
        self.card_game = CardGame()

    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.ace))

    def test_highest_card(self):
        self.assertEqual(self.card2, self.card_game.highest_card(self.ace, self.card2))

    def test_card_total(self):
        self.assertEqual("You have a total of 6", self.card_game.cards_total([self.ace, self.card2]))