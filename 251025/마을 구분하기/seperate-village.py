n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def in_range(x, y):
    return x>=0 and x <n and y>=0 and y<n

def can_go(x, y):
    if not in_range(x,y):
        return False
    if grid[x][y] == 0 or visited[x][y]:
        return False
    return True

# U R D L
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

cluster_cnt = 0
val_per_cluster = {}

def dfs(x,y, cluster_cnt):
    for dx, dy in zip(dxs, dys):
        if can_go(x+dx, y+dy):
            visited[x+dx][y+dy] = 1
            val_per_cluster[cluster_cnt] += 1
            dfs(x+dx, y+dy, cluster_cnt)

for x in range(n):
    for y in range(n):
        if not visited[x][y] and grid[x][y] == 1:
            visited[x][y] = 1
            cluster_cnt +=1
            val_per_cluster[cluster_cnt] = 1
            dfs(x, y, cluster_cnt)

print(cluster_cnt)
for item in sorted(val_per_cluster.values()):
    print(item)



