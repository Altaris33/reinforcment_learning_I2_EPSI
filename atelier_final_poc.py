# test Reinforcment learning Python
import numpy as np 
import logging
from random import randint
from enum import Enum, IntEnum

class EnvironmentLabyrinthGrid(object):
    
    labyrinth_version: tuple = ("1", "2", "3")
    
    def __init__(self, labyrinthCoordinates):
        self.labyrinthCoordinates = labyrinth
    
    ACTIONS: list = [
            [-1,0],
            [1,0],
            [0,-1],
            [0,1]
        ]
    
    start_position = [0,0]
    # reset()

    def __str__(self):
        return f'Labyrinth grid: {self.labyrinthCoordinates}'

    def __repr__(self):
      return f'<Labyrinth: {self.labyrinthCoordinates}>'

    @classmethod
    def get_labyrinth_version(cls, labyrinthCoordinates):
      return cls(labyrinthCoordinates, cls.labyrinth_version[0])    

    def print_labyrinth_coordinates_beautified(self):
        """

        Returns the labyrinth as a visual 2D grid
        -------
        None.

        """
      for item in labyrinth:
        if not item == -1:
            separator = '    '
        else:
            separator = ' '    
        print(*item, sep=separator)
        
    def reset(self):
        """
        Resets the agent's position

        Returns
        -------
        None.

        """
        self.x = self.start_position[0]
        self.y = self.start_position[1]

    def take_action():
        pass 

if __name__ == '__main__':
    labyrinth: list = [
      [-1, -1, -1, -1, -1, -1, -1],
      [-1, 0, -1, -1, -1, -1, -1],
      [-1, -1, -1, -1, -1, -1, -1],
      [-1, -1, -1, -1, -1,  2, -1],
      [-1, -1, -1, -1, -1, -1, -1],
      [-1, -1, -1, -1, -1, -1, -1],
      [-1, -1, -1, -1, -1, -1, -1],
      [-1, -1, -1, -1, -1, -1, -1]
    ]
    labyrinthGrid = EnvironmentLabyrinthGrid(labyrinth)
    print(labyrinthGrid)
    labyrinthGrid.print_labyrinth_coordinates_beautified()
    
    q_table = np.array(row for row in range(0,36))
    print(f'Generated Q Table: {q_table}')