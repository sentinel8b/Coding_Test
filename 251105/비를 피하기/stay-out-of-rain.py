from collections import deque

n, h, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
step_map = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] == 1:
        return False
    return True


dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

h_coord_list = []
h_min_dist_list = []
# find human coord and bfs
bfs_q = deque()

for x in range(n):
    for y in range(n):
        if grid[x][y] == 2:
            bfs_q.clear()
            is_found = False
            bfs_q.append((x,y,0))
            visited = [[0] * n for _ in range(n)]
            visited[x][y] = 1
            while bfs_q:
                curr_x, curr_y, step = bfs_q.popleft()
                if grid[curr_x][curr_y] == 3:
                    step_map[x][y] = step
                    is_found = True
                    break
                for dx, dy in zip(dxs, dys):
                    nx, ny = curr_x + dx, curr_y + dy
                    if can_go(nx,ny):
                        visited[nx][ny] = 1
                        bfs_q.append((nx,ny,step+1))

            if not is_found:
                step_map[x][y] = -1

for row in step_map:
    print(*row)
