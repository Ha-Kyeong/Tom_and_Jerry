'''
This module is for returning current position and heading to the next position, 
by determining the direction you would choose to go. You have to determine the direction. 
'''
from typing import List
from view_map import initial_Map
import random

'''
    ----------------------------------------------
    WARNING
    Do not change class/def name, arguments and return.
    Just fill the designated blank space. 
    ----------------------------------------------
'''

# This class initiates the current position
class Position:
    def __init__(
        self, 
        x: int, 
        y: int
    ) -> None:
        self.current_x = x
        self.current_y = y

# This class determines the direction of path you would take. 
# You have to fill the designated blank space. 
class Shortest_Path_Algorithm(Position):
    def __init__(
        self, 
        x: int, 
        y: int
    ) -> None:
        super().__init__(x, y)
        '''
            If you want to store some values, define your variables here.
            Using `self`-based variables, you can re-call the value of previous state easily.
        '''
        self.dir_x = 0
        self.dir_y = 0
        

    def algorithms(self):
        
        #### Code Here! ####
        
        #THIS IS AN EXAMPLE CODE. DELETE THIS CODE SEGMENT BEFORE YOU START YOUR OWN CODE.
        #START OF EXAMPLE CODE
        
        self.dir_x = 0
        self.dir_y = -1

        if [self.current_x, self.current_y] == [0, 0]:
            self.dir_x = 1
            self.dir_y = 0 

        if self.current_y == 0:
            self.dir_x = 1
            self.dir_y = 0 

        #END OF EXAMPLE CODE

        ######################
        '''
            Tip::
                - Try to avoid loop-based codes such as `while` as possible. It will make the problem harder to solve.
        '''
        ##### DO NOT CHANGE RETURN VARIABLES! #####
        ## The below codes are fixed. The users only determine self.dir_x and self.dir_y, or the next position(coordinate).
        ## Therefore, you need to match the variables of return to simulate.
        next_x = self.current_x + self.dir_x
        next_y = self.current_y + self.dir_y
        return [next_x, next_y] 