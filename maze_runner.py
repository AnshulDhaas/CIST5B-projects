def maze_runner(maze):
    START = (0, 0)
    EXIT = (len(maze) - 1, len(maze[0]) - 1)
    
    def is_valid(x, y):
        
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
    def navigate(x, y):
        #base case: if we reach the exit
        if (x, y) == EXIT:
            maze[x][y] = 2 #mark the path
            return True
        
        if not is_valid(x, y):
            return False
        
        maze[x][y] = 2 #mark the index
        
        for direction in directions:
            new_x = x + direction[0]
            new_y = y + direction[1]
            if navigate(new_x, new_y):
                maze[x][y] = 2
                return True
        maze[x][y] = 0 #if index isn't valid go backwards (we hit a dead end)
        return False
    
    return navigate(START[0], START[1])
        
    
    