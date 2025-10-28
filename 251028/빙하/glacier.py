from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def check_neighbor(x,y):
    is_valid = False
    for dx, dy in zip(dxs, dys):
        if in_range(x+dx, y+dy):
            if grid[x+dx][y+dy] == 0:
                is_valid = True
    return is_valid

# init bfs_queue
def register_bfs_q():
    bfs_q = deque()
    cnt_ice = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y] == 0 and check_neighbor(x,y):
                bfs_q.append((x,y))
            if grid[x][y] == 1:
                cnt_ice += 1
    return bfs_q, cnt_ice

t = 0
prev_ice = 0
while True:
    bfs_q, cnt_ice = register_bfs_q()

    if cnt_ice == 0:
        break
    else:
        prev_ice = cnt_ice
    while bfs_q:
        x, y = bfs_q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny):
                if grid[nx][ny] == 1:
                    grid[nx][ny] = 0
    t += 1

print(t, prev_ice)






