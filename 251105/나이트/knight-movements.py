from collections import deque

n = int(input())

r1, c1, r2, c2 = map(int, input().split())
visited = [[0] * n for _ in range(n)]
step_map = [[0] * n for _ in range(n)]

dxs = [-2, -1, 1, 2, 2, 1, -1, -2]
dys = [1, 2, 2, 1, -1, -2, -2, -1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def can_go(x, y):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False
    
    return True

# zero based idx
r1, c1 = r1-1, c1-1
r2, c2 = r2-1, c2-1

bfs_q = deque()
bfs_q.append((r1, c1, 0))
visited[r1][c1] = 1

while bfs_q:
    x, y, step = bfs_q.popleft()
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx, ny):
            visited[nx][ny] = 1
            step_map[nx][ny] = step+1
            bfs_q.append((nx, ny, step+1))

if not visited[r2][c2]:
    print(-1)
else:
    print(step_map[r2][c2])
            