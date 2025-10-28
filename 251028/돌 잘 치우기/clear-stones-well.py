import itertools
from copy import deepcopy
from collections import deque

n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
pts = [list(map(int, input().split())) for _ in range(k)]

def in_range(x, y):
    return 0<= x < n and 0<= y <n

def bfs(start_points, grid_for_bfs, visited_for_bfs):
    # U R D L
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]

    bfs_q = deque()
    for point in start_points:
        x, y = point[0] - 1, point[1] - 1
        
        if grid_for_bfs[x][y] == 0 and not visited_for_bfs[x][y]:
            bfs_q.append((x, y))
            visited_for_bfs[x][y] = 1 

    # 3. BFS 실행 (이 부분은 거의 동일)
    while bfs_q:
        x, y = bfs_q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny, grid_for_bfs, visited_for_bfs): 
                visited_for_bfs[nx][ny] = 1 # 
                bfs_q.append((nx, ny))

def can_go(x, y, grid, visited):
    if not in_range(x, y):
        return False
    if visited[x][y]: # 
        return False
    if grid[x][y] == 1:
        return False
    return True

def get_stone_coord_list(grid):
    coord_list = []
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 1:
                coord_list.append((x,y))
    return coord_list


stone_coord_list = get_stone_coord_list(grid)
stone_combs = itertools.combinations(stone_coord_list, m)

max_val = 0

for comb in stone_combs:
    temp_grid = deepcopy(grid) 
    global_visited = [[0] * n for _ in range(n)]
    case_val = 0

    for stone_coord in comb:
        stone_x, stone_y = stone_coord
        temp_grid[stone_x][stone_y] = 0

    bfs(pts, temp_grid, global_visited)

    for x in range(n):
        for y in range(n):
            if global_visited[x][y] == 1:
                case_val += 1
    max_val = max(case_val, max_val)

print(max_val)