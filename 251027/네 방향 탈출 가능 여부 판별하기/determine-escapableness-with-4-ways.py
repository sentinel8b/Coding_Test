from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visitied = [[0]*m for _ in range(n)] 
# U R D L
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visitied[x][y] or grid[x][y] == 0:
        return False
    return True
    
def push(x,y):
    q.append((x,y))

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx,ny):
                push(nx, ny)
                visitied[nx][ny] = 1

q = deque()
push(0,0)
visitied[0][0] = 1
bfs()

if visitied[n-1][m-1]:
    print(1)
else:
    print(0)


