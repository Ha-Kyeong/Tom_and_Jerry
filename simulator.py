'''
This module simulates the game, using simul() function.
And under specific cases, the simulation should be ended using terminate() function.
'''
from typing import List
from view_map import initial_Map, final_Map, map
from fill_your_algorithm import Position, Shortest_Path_Algorithm
from move import MoveNext

# Tom and Jerry's initial position
global Tom_src, Jerry_dst
GV_object = initial_Map()
[Tom_src, Jerry_dst] = GV_object.Tom_Jerry_Position()

# The trace of coordinates of path
global path_list
path_list = []


# This function makes the variable 'the_end' True, when the simulation should be ended.
def terminate(current_x, current_y, next_x, next_y, path_len, error_flag) -> bool:
    the_end = False

    # When path reaches Jerry
    if [current_x, current_y] == Jerry_dst:
        the_end = True

    # When variable 'error_flag' is true 
    elif error_flag:
        the_end = True

    # When Tom attemps to move more than 2 cells at a time
    elif (abs(current_x-next_x) + abs(current_y-next_y)) > 1:
        the_end = True

    # When path is iterating(wandering in infinite loop)...
    elif path_len >= 1000:
        the_end = True

    return the_end

  
# This function simulates the game, by using classes in other modules. 
def simul():
    # The lenth of path
    global path_len
    path_len = 0

    # Initial current position
    position = Shortest_Path_Algorithm(Tom_src[0], Tom_src[1])
    print("Starting from:", Tom_src)

    # Iteration of each move
    while(True):
        next_x, next_y = position.algorithms()
        
        move_next = MoveNext(next_x, next_y)

        if terminate(
            position.current_x, 
            position.current_y, 
            next_x, 
            next_y, 
            path_len, 
            move_next.check_out_of_map()
            ) == True:
            print('\n')
            final_map = final_Map(path_list)

            # When path reaches Jerry
            if [position.current_x, position.current_y] == Jerry_dst:
                print("I Caught you!!")
                print(f'path length: {path_len}')
                print('Did Tom reach Jerry?: Yes')

            # When variable 'move_next.check_out_of_map()' is true 
            elif move_next.check_out_of_map():
                print("Cannot go ahead")
                print(f'path length: {path_len}')
                print('Did Tom reach Jerry?: No')

            # When Tom attemps to move more than 2 cells at a time
            elif (abs(position.current_x-next_x) + abs(position.current_y-next_y)) > 1:
                print("Can only move by 1")
                print(f'path length: {path_len}')
                print('Did Tom reach Jerry?: No')

            # When path is iterating(wandering in infinite loop)...
            elif path_len >= 1000:
                print("Path is never-ending")
                print(f'path length: {path_len}')
                print('Did Tom reach Jerry?: NO')

            exit()
        
        # Update current position
        position = Shortest_Path_Algorithm(next_x, next_y)

        # Print coordinate on the terminal 
        print('->', end='')
        print([next_x, next_y], end='')

        path_list.append([next_x, next_y])
        path_len += 1  