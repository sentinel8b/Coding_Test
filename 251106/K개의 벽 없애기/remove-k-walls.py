from itertools import combinations
from collections import deque
from copy import deepcopy

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1, c1 = r1-1, c1-1
r2, c2 = r2-1, c2-1

wall_coord_list = []
for x in range(n):
    for y in range(n):
        if grid[x][y] == 1:
            wall_coord_list.append((x,y))

# U R D L
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y,grid,visited):
    if not in_range(x,y):
        return False
    if grid[x][y] == 1:
        return False
    if visited[x][y]:
        return False
    
    return True

ans = 100000

# select k walls among all walls
comb_list = combinations(wall_coord_list, k)

for comb in comb_list:
    temp_grid = deepcopy(grid)
    visited = [[0]*n for _ in range(n)]

    #break the coord
    for coord in comb:
        x, y = coord
        temp_grid[x][y] = 0

    bfs_q = deque()
    bfs_q.append((r1,c1,0))
    visited[r1][c1] = 1
    
    while bfs_q:
        x, y, step = bfs_q.popleft()
        if x == r2 and y == c2:
            ans = min(ans, step)
            break
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny,temp_grid,visited):
                visited[nx][ny] = 1
                bfs_q.append((nx, ny, step+1))


if ans == 100000:
    print(-1)
else:
    print(ans)