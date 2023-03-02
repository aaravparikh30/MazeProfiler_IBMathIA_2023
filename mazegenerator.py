import random
import sys

def generate_maze_solvable(n, m):
    sys.setrecursionlimit(n*m)
    maze = [['#' for x in range(m)] for y in range(n)]
    x, y = 0, 0
    maze[y][x] = 'S'
    generate_maze_recursive(maze, x, y)
    maze[n-1][m-1] = 'E'
    # Removing walls around S and E
    maze[0][1] = "."
    maze[1][0] = "."
    maze[n-1][m-2] = "."
    maze[n-2][m-1] = "."
    return maze





def generate_maze_recursive(maze, x, y):
    directions = ["N", "S", "E", "W"]
    random.shuffle(directions)
    for direction in directions:
        if direction == "N":
            if y-2 <= 0:
                continue
            if maze[y-2][x] == "#":
                maze[y-2][x] = "."
                maze[y-1][x] = "."
                generate_maze_recursive(maze, x, y-2)
        elif direction == "S":
            if y+2 >= len(maze)-1:
                continue
            if maze[y+2][x] == "#":
                maze[y+2][x] = "."
                maze[y+1][x] = "."
                generate_maze_recursive(maze, x, y+2)
        elif direction == "E":
            if x+2 >= len(maze[0])-1:
                continue
            if maze[y][x+2] == "#":
                maze[y][x+2] = "."
                maze[y][x+1] = "."
                generate_maze_recursive(maze, x+2, y)
        elif direction == "W":
            if x-2 <= 0:
                continue
            if maze[y][x-2] == "#":
                maze[y][x-2] = "."
                maze[y][x-1] = "."
                generate_maze_recursive(maze, x-2, y)
maze = generate_maze_solvable(5, 5)
for row in maze:
    print(row)
