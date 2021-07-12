import random

class Deck:
   def __init__(self):
      self.deck = []
      self.initializeDeck()
      self.discard = []
   
   def initializeDeck(self):
      self.addCards('pink')
      self.addCards('white')
      self.addCards('blue')
      self.addCards('yellow')
      self.addCards('orange')
      self.addCards('black')
      self.addCards('red')
      self.addCards('green')
      self.addCards('', 14) #wild card, will match any color
      self.shuffleDeck()

   def shuffleDeck(self):
      new_deck = []
      while len(self.deck) > 0:
         random_index = random.randint(0, len(self.deck) - 1)
         new_deck.append(self.deck.pop(random_index))
      self.deck = new_deck.copy()

   def addCards(self, color, num_of_card=12):
      for i in range(num_of_card):
         self.deck.append(Card(color))

   def drawCard(self):
      if (len(self.deck == 0)):
         self.deck = self.discard.copy()
         self.discard.clear()
         self.shuffleDeck()
      return self.deck.pop()
   
   def addToDiscard(self, card):
      self.discard.append(card)

class Card:
   def __init__(self, color):
      self._color = color
   
   def getColor(self):
      return self._color

   def __repr__(self):
      return self.getColor()