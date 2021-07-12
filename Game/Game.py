from Game.Board import Board
from Game.Deck import Deck

class Game:
   def __init__(self):
      self.board = Board()
      self.deck = Deck()
      print(len(self.deck.deck))