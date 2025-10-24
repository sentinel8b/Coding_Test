n, m = map(int, input().split())

if n == 1:
    print(0)
    exit()

adj_mat = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    adj_mat[start][end] = 1
    adj_mat[end][start] = 1

node_cnt = 0
visitied = [False] * (n+1)

def dfs(start_idx):
    global node_cnt 
    global visitied
    for node in range(1, n+1):
        if adj_mat[start_idx][node] and not visitied[node]:
            visitied[node] = True
            dfs(node)

dfs(1)
print(sum(visitied)-1)