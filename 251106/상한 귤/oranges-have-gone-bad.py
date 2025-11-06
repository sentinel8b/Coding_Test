from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
step_map = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] == 0:
        return False
    return True

bfs_q = deque()

for x in range(n):
    for y in range(n):
        if grid[x][y] == 2:
            bfs_q.append((x,y,0))
            visited[x][y] = 1
while bfs_q:
    x, y, step = bfs_q.popleft()
    if grid[x][y] == 1:
        grid[x][y] = 2
        step_map[x][y] = step

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy 
        if can_go(nx, ny):
            bfs_q.append((nx, ny, step+1))
            visited[nx][ny] = 1

for x in range(n):
    for y in range(n):
        if grid[x][y] == 1 and step_map[x][y] == 0:
            step_map[x][y] = -2
        if grid[x][y] == 0 and step_map[x][y] == 0:
            step_map[x][y] = -1
            
for row in step_map:
    print(*row)
