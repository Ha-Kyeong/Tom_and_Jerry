## 1. Intro
This game is named as "Tom and Jerry Game". The cat (Tom) at the starting point should find the most effective path(that is, the shortest path) to the mouse (Jerry) at the destination. You have to develop your own algorithm to perform the task. 

## 2. How does the game work
### 1. Map  
The map consists of 4 components.  
  
🐈 : This is Tom. Tom is located at certain position on the map.  
🐀 : This is Jerry. Jerry is located at certain position on the map.  
⬜ : This is cell. Tom can pass it through.  
🔵 : This is obstacle. Tom has to find path around the obstacle, since he cannot pass it through.  

### 2. Simulation
You can simulate the game on the terminal window by simulating "main.py" module. Once simulated, map information and the result are shown on the map.  
This is how the result is shown on the terminal. 

>>> Tom & Jerry <<< 
[Simulator]
 - Start Postion: [0, 14]
 - End Postion: [14, 0]
[Map]
 - Map Size: 15 * 15
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🐀
⬜🔵⬜⬜⬜⬜🔵⬜⬜⬜⬜⬜🔵🔵⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🔵🔵⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🔵🔵⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🔵🔵⬜
⬜🔵⬜⬜⬜⬜🔵⬜⬜⬜⬜⬜🔵🔵⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🔵🔵⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜🔵🔵⬜⬜⬜🔵⬜🔵⬜⬜
⬜⬜⬜⬜⬜🔵🔵⬜⬜⬜🔵⬜🔵⬜⬜
⬜⬜⬜🔵⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜🔵⬜⬜🔵⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜🔵⬜⬜🔵⬜⬜⬜⬜⬜🔵⬜🔵⬜⬜
🐈⬜⬜🔵⬜⬜⬜⬜⬜⬜🔵⬜🔵⬜⬜

Starting from: [0, 14]
->[0, 13]->[0, 12]->[0, 11]->[0, 10]->[0, 9]->[0, 8]->[0, 7]->[0, 6]->[0, 5]->[0, 4]->[0, 3]->[0, 2]->[0, 1]->[0, 
0]->[1, 0]->[2, 0]->[3, 0]->[4, 0]->[5, 0]->[6, 0]->[7, 0]->[8, 0]->[9, 0]->[10, 0]->[11, 0]->[12, 0]->[13, 0]->[14, 0]

............................🐀
..🔵⬜⬜⬜⬜🔵⬜⬜⬜⬜⬜🔵🔵⬜
..⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🔵🔵⬜
..⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🔵🔵⬜
..⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🔵🔵⬜
..🔵⬜⬜⬜⬜🔵⬜⬜⬜⬜⬜🔵🔵⬜
..⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🔵🔵⬜
..⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
..⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
..⬜⬜⬜⬜🔵🔵⬜⬜⬜🔵⬜🔵⬜⬜
..⬜⬜⬜⬜🔵🔵⬜⬜⬜🔵⬜🔵⬜⬜
..⬜⬜🔵⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
..⬜🔵⬜⬜🔵⬜⬜⬜⬜⬜⬜⬜⬜⬜
..🔵⬜⬜🔵⬜⬜⬜⬜⬜🔵⬜🔵⬜⬜
🐈⬜⬜🔵⬜⬜⬜⬜⬜⬜🔵⬜🔵⬜⬜
I Caught you!!
path length: 28
Did Tom reach Jerry?: Yes

## 3. Guideline for Environment setting

