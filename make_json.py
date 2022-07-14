'''
This module is for makeing a map: defining map size, position of the obstacles.
This module converts python object('map') into JSON data(Encoding). 
'''
import json
from math import inf

map = {
    "1.Width": 15,
    "2.Height": 15,
    "3.Cell": [
        [0,inf,0,0,0,0,inf,0,0,0,0,0,0,0,'Jerry'],
        [0,0,0,0,0,0,0,0,0,0,0,0,inf,inf,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,inf,inf,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,inf,inf,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,inf,inf,0],
        [0,inf,0,0,0,0,inf,0,0,0,0,0,inf,inf,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,inf,inf,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,inf,inf,0,0,0,inf,0,inf,0,0],
        [0,0,0,0,0,inf,inf,0,0,0,inf,0,inf,0,0],
        [0,0,0,inf,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,inf,0,0,inf,0,0,0,0,0,0,0,0,0],
        [0,inf,0,0,inf,0,0,0,0,0,inf,0,inf,0,0],
        ['Tom',0,0,inf,0,0,0,0,0,0,inf,0,inf,0,0]
        ]
}

map_json = json.dumps(map, indent=4, sort_keys=True)