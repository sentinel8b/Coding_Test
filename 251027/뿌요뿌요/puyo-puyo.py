n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x,y, val):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] != val:
        return False
    return True

# U R D L
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def dfs(x,y, val):
    global local_cluster_size
    for dx, dy in zip(dxs, dys):
        if can_go(x+dx,y+dy,val):
            visited[x+dx][y+dy] = 1
            local_cluster_size += 1
            dfs(x+dx,y+dy,val)


cluster_num = 0
max_cluster_size = 0

for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            visited[x][y] = 1
            local_cluster_size = 1
            cur_val = grid[x][y]
            dfs(x,y,cur_val)
            if local_cluster_size >= 4:
                cluster_num += 1
            max_cluster_size = max(max_cluster_size, local_cluster_size)

print(cluster_num, max_cluster_size)

