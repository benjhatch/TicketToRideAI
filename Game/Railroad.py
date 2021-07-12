class Railroad:
   def __init__(self, length, colors, num_of_tracks=1):
      self._length = length
      self._colors = colors
      self._num_of_tracks = num_of_tracks

   def canFill(self, num_of_cards, color):
      return ((self.getNumOfTracks() > 0) & (color in self.getColors()) & (num_of_cards == self.getLength()))

   def fillTrack(self, color):
      self.getColors().remove(color)
      self._num_of_tracks -= 1

   def isFull(self):
      return self.getNumOfTracks() <= 0

   def getNumOfTracks(self):
      return self._num_of_tracks
   
   def getColors(self):
      return self._colors

   def getLength(self):
      return self._length
   
   def __repr__(self):
      return str(self.getNumOfTracks())