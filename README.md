## 1. Intro
This game is named as "Tom and Jerry Game". 

The cat (Tom) at the starting point should find the most effective path(that is, the shortest path) to the mouse (Jerry) at the destination. You have to develop your own algorithm to perform the task.  


## 2. How does the game work
### 1. Map  
The map consists of 4 components.  
  
🐈 : This is Tom. Tom is located at certain position on the map.  
🐀 : This is Jerry. Jerry is located at certain position on the map.  
⬜ : This is cell. Tom can pass it through.  
🔵 : This is obstacle. Tom has to find path around the obstacle, since he cannot pass it through.  

Once cells are selected as path, those cells appear as '..' on the final map. 

### 2. Simulation
Run `main.py` module to simulate the game. Once simulated, following results appear on the terminal.
+ information and graphics of the initial map 
+ coordinates of the path that Tom has taken
+ graphics and evaluation of the final map 
  
For example, this is how the results are shown on the terminal.
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

### 3. Code your algorithm
In `fill_your_algorithm.py` module, complete the method `algorithms` in the class `Shortest_Path_Algorithm`. You have to code for 'self.dir_x' and 'self.dir_y' to determine the next position.
``` python
class Shortest_Path_Algorithm(Position):
    def __init__(self, x: int, y: int) -> None: 
        super().__init__(x, y)
        '''
            If you want to store some values, define your variables here.
            Using `self`-based variables, you can re-call the value of previous state easily.
        '''
        self.dir_x = 0
        self.dir_y = 0
        

    def algorithms(self):
        
        #### Code Here! ####
```
  
WARNING: Do not change class/def name, arguments and return. Just fill the designated blank space.


## 3. Guideline for Environment setting
Since this game only contains Python Standard Libraries (that is, automatically installed libraries when you installed python), you don't have to install any 3rd Party libraries. Therefore, you don't need to worry about the version setting or any conflict resulting from it.  
There are two ways to simulate the game on your pc.  
### 1. Use git and VSCode
Install git and VSCode.  

+ How to install git: https://taewow.tistory.com/13  
+ How to install VSCode: https://velog.io/@eunyeong560/Visual-Studio-Code-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-%EB%B0%8F-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95

After installing git and VSCode, type this instruction on the terminal 

    git clone https://github.com/Ha-Kyeong/Tom_and_Jerry.git
    
Then, the files will be automatically pulled to your pc.
    
### 2. Download the zip file provided in the link below
You can munually download the files on your pc. Be careful not to contain Hangeul letters in your directory address.

Download zip file: https://drive.google.com/file/d/15yt0hRswq2PUtPMupbRwa595ufdp7Pgo/view?usp=sharing  


## 4. If you have any questions 
Feel free to ask me at any time. You can contact me via mobile message, or email. 
