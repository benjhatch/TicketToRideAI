from Game.City import City
from Game.Railroad import Railroad

# This Board is configured for
# the traditional Ticket to Ride
# Game (which takes place in the
# USA)
class Board:
   def __init__(self):
      self._cities = {}
      self._city_names = ['Vancouver', 'Calgary', 'Winnipeg', 
      'Sault St. Marie', 'Montreal', 'Boston', 'Toronto', 
      'Seattle', 'Helena', 'Duluth', 'Portland', 'New York',
      'San Francisco', 'Salt Lake City', 'Denver', 'Omaha',
      'Chicago', 'Pittsburgh', 'Washington', 'Kansas City',
      'Saint Louis', 'Nashville', 'Raleigh', 'Atlanta',
      'Charleston', 'Los Angeles', 'Las Vegas', 'Phoenix',
      'Santa Fe', 'Oklahoma City', 'Little Rock', 'El Paso',
      'Dallas', 'Houston', 'New Orleans', 'Miami'];
      self.createCities()
      # railroads represented using an adjacency matrix
      self.createRailroadGraph()

   def getCities(self):
      return self._cities

   def getCityIndex(self, city_name):
      return self._city_names.index(city_name)
   
   def createCities(self):
      for city_name in self._city_names:
         self.initializeCity(city_name)

   def initializeCity(self, city_name):
      self.getCities()[city_name] = City(city_name)

   def logCities(self):
      print('Number of cities: {0}'.format(len(self.getCities())))
      for city_name in self.getCities().keys():
         print(self.getCities()[city_name])
   
   def createRailroadGraph(self):
      self._railroad_graph = self.initializeGraph()

      # any color railroads
      self.linkCity('Vancouver', 'Seattle', 1, ['gray'], 2)
      self.linkCity('Vancouver', 'Calgary', 3, ['gray'])
      self.linkCity('Calgary', 'Seattle', 4, ['gray'])
      self.linkCity('Seattle', 'Portland', 1, ['gray'], 2)
      self.linkCity('Calgary', 'Helena', 4, ['gray'])
      self.linkCity('Winnipeg', 'Sault St. Marie', 6, ['gray'])
      self.linkCity('Sault St. Marie', 'Duluth', 3, ['gray'])
      self.linkCity('Sault St. Marie', 'Toronto', 2, ['gray'])
      self.linkCity('Toronto', 'Montreal', 3, ['gray'])
      self.linkCity('Toronto', 'Pittsburgh', 2, ['gray'])
      self.linkCity('Montreal', 'Boston', 2, ['gray'], 2)
      self.linkCity('Pittsburgh', 'Washington', 2, ['gray'])
      self.linkCity('Pittsburgh', 'Raleigh', 2, ['gray'])
      self.linkCity('Raleigh', 'Washington', 2, ['gray'], 2)
      self.linkCity('Raleigh', 'Charleston', 2, ['gray'])
      self.linkCity('Raleigh', 'Atlanta', 2, ['gray'], 2)
      self.linkCity('Atlanta', 'Charleston', 2, ['gray'])
      self.linkCity('Atlanta', 'Nashville', 1, ['gray'])
      self.linkCity('Nashville', 'Saint Louis', 2, ['gray'])
      self.linkCity('Saint Louis', 'Little Rock', 2, ['gray'])
      self.linkCity('Little Rock', 'Oklahoma City', 2, ['gray'])
      self.linkCity('Little Rock', 'Dallas', 2, ['gray'])
      self.linkCity('Houston', 'New Orleans', 2, ['gray'])
      self.linkCity('Houston', 'Dallas', 1, ['gray'], 2)
      self.linkCity('Dallas', 'Little Rock', 2, ['gray'])
      self.linkCity('Dallas', 'Oklahoma City', 2, ['gray'], 2)
      self.linkCity('Kansas City', 'Oklahoma City', 2, ['gray'], 2)
      self.linkCity('Kansas City', 'Omaha', 1, ['gray'], 2)
      self.linkCity('Omaha', 'Duluth', 2, ['gray'], 2)
      self.linkCity('Denver', 'Santa Fe', 2, ['gray'])
      self.linkCity('Santa Fe', 'El Paso', 2, ['gray'])
      self.linkCity('Santa Fe', 'Phoenix', 3, ['gray'])
      self.linkCity('El Paso', 'Phoenix', 3, ['gray'])
      self.linkCity('Los Angeles', 'Phoenix', 3, ['gray'])
      self.linkCity('Los Angeles', 'Las Vegas', 3, ['gray'])

      # white railroads
      self.linkCity('Calgary', 'Winnipeg', 6, ['white']);
      self.linkCity('Phoenix', 'Denver', 5, ['white']);
      self.linkCity('Chicago', 'Toronto', 4, ['white']);
      self.linkCity('Little Rock', 'Nashville', 3, ['white']);

      # green railroads
      self.linkCity('Helena', 'Denver', 4, ['green']);
      self.linkCity('El Paso', 'Houston', 6, ['green']);
      self.linkCity('Little Rock', 'New Orleans', 3, ['green']);
      self.linkCity('Saint Louis', 'Pittsburgh', 5, ['green']);

      # pink railroads
      self.linkCity('Helena', 'Salt Lake City', 3, ['pink']);
      self.linkCity('Denver', 'Omaha', 4, ['pink']);
      self.linkCity('Duluth', 'Toronto', 6, ['pink']);
      self.linkCity('Charleston', 'Miami', 4, ['pink']);

      # yellow railroads
      self.linkCity('Seattle', 'Helena', 6, ['yellow']);
      self.linkCity('El Paso', 'Oklahoma City', 5, ['yellow']);
      self.linkCity('Nashville', 'Pittsburgh', 4, ['yellow']);

      # orange railroads
      self.linkCity('Helena', 'Duluth', 6, ['orange']);
      self.linkCity('Las Vegas', 'Salt Lake City', 3, ['orange']);

      # black railroads
      self.linkCity('Los Angeles', 'El Paso', 6, ['black']);
      self.linkCity('Winnipeg', 'Duluth', 4, ['black']);
      self.linkCity('Sault St. Marie', 'Montreal', 5, ['black']);
      self.linkCity('Nashville', 'Raleigh', 3, ['black']);

      # blue railroads
      self.linkCity('Portland', 'Salt Lake City', 6, ['blue']);
      self.linkCity('Helena', 'Winnipeg', 4, ['blue']);
      self.linkCity('Omaha', 'Chicago', 4, ['blue']);
      self.linkCity('Atlanta', 'Miami', 5, ['blue']);
      self.linkCity('Santa Fe', 'Oklahoma City', 3, ['blue']);
      self.linkCity('New York', 'Montreal', 3, ['blue']);

      # red railroads
      self.linkCity('Denver', 'Oklahoma City', 4, ['red']);
      self.linkCity('El Paso', 'Dallas', 4, ['red']);
      self.linkCity('Helena', 'Omaha', 5, ['red']);
      self.linkCity('Duluth', 'Chicago', 3, ['red']);
      self.linkCity('New Orleans', 'Miami', 6, ['red']);

      # multiple colors
      self.linkCity('San Francisco', 'Salt Lake City', 5, ['white', 'orange'], 2);
      self.linkCity('Chicago', 'Saint Louis', 2, ['white', 'green'], 2);
      self.linkCity('Pittsburgh', 'New York', 2, ['white', 'green'], 2);
      self.linkCity('Portland', 'San Francisco', 5, ['green', 'pink'], 2);
      self.linkCity('Kansas City', 'Saint Louis', 2, ['pink', 'blue'], 2);
      self.linkCity('San Francisco', 'Los Angeles', 3, ['pink', 'yellow'], 2);
      self.linkCity('Salt Lake City', 'Denver', 3, ['yellow', 'red'], 2);
      self.linkCity('New Orleans', 'Atlanta', 4, ['yellow', 'orange'], 2);
      self.linkCity('Boston', 'New York', 2, ['yellow', 'red'], 2);
      self.linkCity('Denver', 'Kansas City', 4, ['orange', 'black'], 2);
      self.linkCity('Chicago', 'Pittsburgh', 3, ['orange', 'black'], 2);
      self.linkCity('New York', 'Washington', 2, ['orange', 'black'], 2);


   def linkCity(self, city1_name, city2_name, length, color, num_of_tracks=1):
      railroad = Railroad(length, color, num_of_tracks)
      city1_index = self.getCityIndex(city1_name)
      city2_index = self.getCityIndex(city2_name)
      if (city1_index == -1 | city2_index == -1):
         IndexError()
      self._railroad_graph[city1_index][city2_index] = railroad
      self._railroad_graph[city2_index][city1_index] = railroad

   def getConnections(self):
      visitedRailroads = set()
      for i in range(len(self._railroad_graph)):
         for j in range(len(self._railroad_graph[i])):
            railroad = self._railroad_graph[i][j]
            if (railroad != 0):
               if ((not railroad in visitedRailroads) & (not railroad.isFull())):
                  visitedRailroads.add(railroad)
                  print(self._city_names[i], self._city_names[j], railroad.getLength(), railroad.getColors(), railroad.getNumOfTracks())

   def initializeGraph(self):
      size = len(self.getCities());
      return [[0 for i in range(size)] for j in range(size)]

   def printRailroadGraph(self):
      for row in self._railroad_graph:
         print(row)