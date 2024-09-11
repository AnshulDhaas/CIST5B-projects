def maze_runner(maze):
    START = (0, 0)
    EXIT = (len(maze) - 1, len(maze[0]) - 1)
    
    def is_valid(x, y):
        
    def navigate(x, y):
        #base case: if we reach the exit
        if (x, y) == EXIT:
            maze[x][y] = 2
            return True
        
        if not is_valid(x, y):
            return False
        
        for 
    #recursive case: if the position is valid
    
    #mark the index
    
    #if we hit a wall/no path is found, backtrack and change the cell back to 0