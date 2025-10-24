n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited_grid = [[0]*m for _ in range(n)]

#D R
dxs = [1, 0] 
dys = [0, 1]

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x,y):
    if not in_range(x, y):
        return False
    if visited_grid[x][y] == 1:
        return False
    if grid[x][y] == 0:
        return False
    return True

def dfs(x,y):
    for dx, dy in zip(dxs, dys):
        if can_go(x+dx, y+dy):
            visited_grid[x+dx][y+dy] = 1
            dfs(x+dx, y+dy)

visited_grid[0][0] = 1
dfs(0,0)
if visited_grid[n-1][m-1]:
    print(1)
else:
    print(0)