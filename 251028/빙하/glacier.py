from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def find_external():
    bfs_q = deque()
    bfs_q.append((0,0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    while bfs_q:
        x, y = bfs_q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = 1
                bfs_q.append((nx, ny))

    return visited

def in_range(x,y):
    return 0<=x<n and 0<=y<m


t = 0
prev_ice = 0

while True:
    cnt_ice = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                cnt_ice += 1

    if cnt_ice == 0:
        break
    else:
        prev_ice = cnt_ice

    external_visited = find_external()

    melt_list = []
    for x in range(n):
        for y in range(m):
            if grid[x][y] == 1:
                is_exposed = False
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy
                    if in_range(nx, ny) and external_visited[nx][ny] == 1:
                        is_exposed = True
                        melt_list.append((x,y))

    for x, y in melt_list:
        grid[x][y] = 0
    t+=1

print(t, prev_ice)