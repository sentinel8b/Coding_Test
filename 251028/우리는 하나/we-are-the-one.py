from itertools import combinations
from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# U R D L
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def create_coord_list(n):
    coord_list = []
    for i in range(n):
        for j in range(n):
            coord_list.append((i,j))
    return coord_list

def in_range(x, y):
    return 0<=x<n and 0<=y<n 

def can_go(x,y,nx,ny):
    if not in_range(nx,ny):
        return False
    if visited[nx][ny]:
        return False
    if abs(grid[nx][ny] - grid[x][y]) < u or abs(grid[nx][ny] - grid[x][y]) > d:
        return False
    
    return True


all_coord_list = create_coord_list(n)
coord_combs = combinations(all_coord_list, k)

ans = 0

for comb in coord_combs:
    bfs_q = deque()
    case_cnt = 0
    visited = [[0] * n for _ in range(n)]
    for coord in comb:
        bfs_q.append(coord)
        visited[coord[0]][coord[1]] = 1
        case_cnt += 1
    while bfs_q:
        x, y = bfs_q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x+dx 
            ny = y+dy 
            if can_go(x,y, nx,ny):
                visited[nx][ny] = 1
                case_cnt += 1
                bfs_q.append((nx, ny))

    ans = max(ans, case_cnt)

print(ans)