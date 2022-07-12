'''
This module tells whether the next position is valid or not. 
If the next position is out of map or there's an obstacle in that position, Tom cannot move.
'''
from math import inf
from typing import List
from view_map import initial_Map, map
from fill_your_algorithm import Position, Shortest_Path_Algorithm

# This class determines whether the next position is valid or not. 
class MoveNext:
    def __init__(
        self, 
        x: int, 
        y: int
    ) -> None:
        # visible to User
        self.next_x = x
        self.next_y = y


    def check_out_of_map(self):
        '''
            check if the next position is out of map(out of width/height range of map) 
            or if there is any obstacle in the next position.
        '''
        is_out_map = False
        is_obstacle = False

        # If next position is out of map
        if self.next_x >= map["1.Width"] or self.next_x < 0:
            is_out_map = True
        if self.next_y >= map["2.Height"] or self.next_y < 0:
            is_out_map = True

        # If there is an obstacle in the next position
        if not is_out_map:
            if map["3.Cell"][self.next_y][self.next_x] == inf:
                is_obstacle = True

        # If either of these cases is true, 'cannot_move' is true
        global cannot_move
        cannot_move = is_out_map or is_obstacle
        return cannot_move