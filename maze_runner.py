def maze_runner(maze):
    START = (0, 0)
    EXIT = (len(maze) - 1, len(maze[0]) - 1)
    
    def is_valid(x, y):
        # it's within the maze boundaries and it's not visited or a wall
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

# Example maze
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
# Expected output: A valid path should be found.

# Run the maze solver
result = maze_runner(maze1)
if result:
    for row in result:
        print(row)
else:
    print("No path found")
