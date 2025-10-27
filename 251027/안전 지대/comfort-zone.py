import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m

def can_go(x,y,k):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] <= k:
        return False
    return True

# U R D L
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def dfs(x,y,k):
    visited[x][y] = 1
    for dx, dy in zip(dxs, dys):
        if can_go(x+dx, y+dy,k):
            dfs(x+dx, y+dy,k)

result = []

min_k = 1
ans_safe_cluster = 0

for k in range(1,101):
    safe_cluster = 0
    visited = [[0] * m for _ in range(n)]
    flag = False
    for x in range(n):
        for y in range(m):
            if can_go(x,y,k):
                flag = True
                safe_cluster+=1
                visited[x][y] = 1
                dfs(x,y,k)
                if safe_cluster > ans_safe_cluster:
                    ans_safe_cluster = safe_cluster
                    min_k = k

print(min_k, ans_safe_cluster)