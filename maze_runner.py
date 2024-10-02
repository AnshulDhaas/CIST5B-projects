
def maze_runner(maze):
    START = (0, 0) #START
    EXIT = (len(maze) - 1, len(maze[0]) - 1) #END
    
    def is_valid(x, y):
        # if x or y is in bounds of the 2D array, the index has a value of 0
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0
        
    def navigate(x, y):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # base case: if we reach the exit
        if (x, y) == EXIT:
            maze[x][y] = 2  # mark the path
            return True
        
        if not is_valid(x, y):
            return False
        
        maze[x][y] = 2  # mark the index as part of the path
        
        for direction in directions:
            new_x = x + direction[0]
            new_y = y + direction[1]
            if navigate(new_x, new_y):
                return True
        
        maze[x][y] = 0  # if index isn't valid, go backwards (we hit a dead end)
        return False
    
    if navigate(START[0], START[1]):
        return maze  # If path is found, return the maze with the marked path
    else:
        return False  # No path found

# Example mazes/test cases
maze1 = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
]

maze2 = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

maze3 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

maze4 = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0]
]

maze5 = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
]
#Output
result = maze_runner(maze3)
if result:
    for row in result:
        print(row)
else:
    print("No path found")
    
'''
Write up:
- Beyond this use case, we can use AI to solve mazes using more efficient algorithms, and maybe even make this maze solver more interactive.
- We can also use AI to make this code more interactive with users, maybe even make a GUI or a game for it.
- If the user can't solve it, we can use this algorithm to solve it instead and move on to the next level/step of the game.

'''
