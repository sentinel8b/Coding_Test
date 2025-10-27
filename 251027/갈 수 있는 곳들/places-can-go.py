n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
pts = [list(map(int, input().split())) for _ in range(k)]
visited = [[0]*n for _ in range(n)]

from collections import deque 

# U R D L
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

def push(x,y):
    q.append((x,y))

def bfs():
    global ans
    while q:
        pt = q.popleft()
        x, y = pt[0], pt[1]
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny):
                visited[nx][ny] = 1
                ans+=1
                push(nx, ny)

# main
q = deque()

ans = 0

for pt in pts: 
    x, y = pt[0]-1, pt[1]-1
    q = deque([(x, y)])
    if not visited[x][y]:
        ans += 1
    visited[x][y]=1
    bfs()

print(ans)