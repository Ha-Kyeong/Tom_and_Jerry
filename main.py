'''
This module is the one you should simulate on the terminal.
'''
import json
from queue import Queue
from view_map import final_Map, initial_Map, map
from fill_your_algorithm import Position, Shortest_Path_Algorithm
from simulator import simul, terminate

# This function prints introducing comments
def introduce():
    # Print introduction
    print(f">>> Tom & Jerry <<< ")
    print(f'[Simulator]')

    GV_object = initial_Map()
    [Tom_src, Jerry_dst] = GV_object.Tom_Jerry_Position()
    print(f' - Start Postion: {Tom_src}')
    print(f' - End Postion: {Jerry_dst}')

    print(f'[Map]')
    print(f' - Map Size: {map["1.Width"]} * {map["2.Height"]}')


if __name__ == '__main__':
    # Print introduction
    introduce()
    
    # Print initial map
    show_map = initial_Map()
    show_map.Print_Map()

    # Simulates game
    simul()
    