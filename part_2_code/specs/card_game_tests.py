import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 7)
        self.card2 = Card("Clubs", 6)
        self.card3 = Card("Spades", 4)
        self.card4 = Card("Diamonds", 1)
        self.cards = (self.card1, self.card2, self.card3)


    def test_card_has_suit(self):
        self.assertEqual("Hearts", self.card1.suit)

   
    def card_has_value(self):
        self.assertEqual(7, self.card1.value)


    def test_check_for_ace(self):
        self.card_game = CardGame() 
        self.assertEqual(1, self.card_game.check_for_ace(self.card4))

    
    def test_highest_card(self):
        self.card_game = CardGame() 
        self.assertEqual(self.card3, self.card_game.highest_card(self.card3, self.card4))

  
    def test_cards_total(self):
        self.card_game = CardGame() 
        self.assertEqual("You have a total of 17", self.card_game.cards_total(self.cards))