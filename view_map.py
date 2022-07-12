'''
This module is for showing graphical map on the terminal, using unicode: 🐈, 🐀, ⬜, 🔵
Here, we bring the JSON data in 'make_json.py' into python object(Decoding)
'''
import json
from math import inf
from typing import Dict, List
from make_json import map_json

# Load JSON data into python object(Decoding)
map = json.loads(map_json)

# Load graphic cells
graphic_design: Dict = {
    # Key           # Value
    'Tom':          '🐈',
    'Jerry':        '🐀',
    'path':         '⬜',
    'obstacle':     '🔵',
    'path_taken':   '..'
}

# This class shows the initial map(original map)
class initial_Map:
    def __init__(self) -> None:
        for y in range(0, map["2.Height"]):
            for x in range(0, map["1.Width"]):
                if map["3.Cell"][y][x] == 0: # There's no obstacle
                    self.cell_expr = graphic_design['path'] # '⬜'
                elif map["3.Cell"][y][x] == inf: # There is an obstacle
                    self.cell_expr = graphic_design['obstacle'] # '🔵'
                elif map["3.Cell"][y][x] == 'Tom': # Here is Tom
                    self.cell_expr = graphic_design['Tom'] # '🐈'
                    global Tom_src
                    Tom_src = [x,y]
                elif map["3.Cell"][y][x] == "Jerry": # Here is Jerry
                    self.cell_expr = graphic_design['Jerry'] # '🐀'
                    global Jerry_dst
                    Jerry_dst = [x,y]


    def Tom_Jerry_Position(self) -> List:
        return [Tom_src, Jerry_dst]

    
    def Print_Map(self) -> None:
        for y in range(0, map["2.Height"]):
            for x in range(0, map["1.Width"]):
                if map["3.Cell"][y][x] == 0: # There's no obstacle
                    self.cell_expr = graphic_design['path'] # '⬜'
                elif map["3.Cell"][y][x] == inf: # There is an obstacle
                    self.cell_expr = graphic_design['obstacle'] # '🔵'
                elif map["3.Cell"][y][x] == 'Tom': # Here is Tom
                    self.cell_expr = graphic_design['Tom'] # '🐈'
                    global Tom_src
                    Tom_src = [y,x]
                elif map["3.Cell"][y][x] == "Jerry": # Here is Jerry
                    self.cell_expr = graphic_design['Jerry'] # '🐀'
                    global Jerry_dst
                    Jerry_dst = [y,x]
                print(self.cell_expr, end="")
            print('')
        print()

# This class shows final map(after cells are selected as path)
class final_Map():
    def __init__(self, path_list: List) -> None:
        for y in range(0, map["2.Height"]):
            for x in range(0, map["1.Width"]):
                if map["3.Cell"][y][x] == 0: # There's no obstacle
                    self.cell_expr = graphic_design['path'] # '⬜'
                    for i in range(len(path_list)): 
                        if path_list[i][1] == x and path_list[i][0] == y: # This cell is taken as path
                            self.cell_expr = graphic_design['path_taken'] # '..'
                elif map["3.Cell"][y][x] == inf: # There is an obstacle
                    self.cell_expr = graphic_design['obstacle'] # '🔵'
                elif map["3.Cell"][y][x] == 'Tom': # Here is Tom
                    self.cell_expr = graphic_design['Tom'] # '🐈'
                    global Tom_src
                    Tom_src = [y,x]
                elif map["3.Cell"][y][x] == "Jerry": # Here is Jerry
                    self.cell_expr = graphic_design['Jerry'] # '🐀'
                    global Jerry_dst
                    Jerry_dst = [y,x]
                
                print(self.cell_expr, end="")
            print('')