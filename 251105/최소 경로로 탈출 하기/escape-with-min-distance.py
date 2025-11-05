from collections import deque

n, m = map(int,input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
step_map = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] == 0:
        return False
    return True

# U R D L
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

bfs_q = deque()

bfs_q.append((0,0,0))
visited[0][0] = 1

while bfs_q:
    x, y, step = bfs_q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = 1
            step_map[nx][ny] = step+1
            bfs_q.append((nx, ny, step+1))

if visited[n-1][m-1] != 0:
    print(step_map[n-1][m-1])
else:
    print(-1)