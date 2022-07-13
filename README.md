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
You can simulate the game on the terminal window by simulating "main.py" module. Once simulated, basic map info & organization and the result is shown on the map.  
This is how the result is shown on the terminal.
```
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
```

## 3. Guideline for Environment setting
Since this game only contains Python Standard Libraries (that is, automatically installed libraries when you installed python), you don't have to install any 3rd Party libraries. Therefore, you don't need to worry about the version setting or any conflict resulting from it.  
There are two ways to conduct this game on your pc.  
### 1. Use git and VSCode

### 2. Make the files manually on your pc  
copy and paste these files and on your pc.
