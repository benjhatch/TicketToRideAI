from Game.Railroad import Railroad

class City:
   def __init__(self, name):
      self._name = name

   def getName(self):
      return self._name

   def __str__(self):
      return self.getName()