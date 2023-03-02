import random
import time

def generate_maze_dfs(n, m):
    maze = [['#' for x in range(m)] for y in range(n)]
    stack = []
    visited = []
    x, y = random.randint(0, n-1), random.randint(0, m-1)
    stack.append((x, y))
    visited.append((x, y))
    while len(stack) > 0:
        x, y = stack[-1]
        neighbours = []
        if x > 0 and (x-1, y) not in visited:
            neighbours.append((x-1, y))
        if x < n-1 and (x+1, y) not in visited:
            neighbours.append((x+1, y))
        if y > 0 and (x, y-1) not in visited:
            neighbours.append((x, y-1))
        if y < m-1 and (x, y+1) not in visited:
            neighbours.append((x, y+1))
        if len(neighbours) > 0:
            nx, ny = random.choice(neighbours)
            maze[x][y] = '.'
            maze[nx][ny] = '.'
            stack.append((nx, ny))
            visited.append((nx, ny))
        else:
            stack.pop()
    maze[0][0] = 'S'
    maze[n-1][m-1] = 'E'
    return maze
    
def solve_maze_bfs(maze):
    n = len(maze)
    m = len(maze[0])
    q = [(0, 0)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1

    while q:
        x, y = q.pop(0)
        if maze[x][y] == "E":
            return True
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0 <= x+dx < n and 0 <= y+dy < m and maze[x+dx][y+dy] != "#" and visited[x+dx][y+dy] != 1:
                q.append((x+dx, y+dy))
                visited[x+dx][y+dy] = 1
    return False

n = 30
m = n

maze = generate_maze_dfs(n, m)

start_time = time.time()
result = solve_maze_bfs(maze)
end_time = time.time()

print("Maze solved:", result)
print("Time taken:", end_time - start_time)

#for row in maze:
    #print([i for i in row])
