n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
node_cnt = 0
visited = [False] *(n+1)

def dfs(node):
    global node_cnt
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            node_cnt += 1
            dfs(neighbor)

for i in range(m):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited[1] = True
dfs(1)

print(node_cnt)

# adj_mat = [[0]*(n+1) for _ in range(n+1)]

# for _ in range(m):
#     start, end = map(int, input().split())
#     adj_mat[start][end] = 1
#     adj_mat[end][start] = 1

# node_cnt = 0
# visitied = [False] * (n+1)

# def dfs(start_idx):
#     global node_cnt 
#     global visitied
#     for node in range(1, n+1):
#         if adj_mat[start_idx][node] and not visitied[node]:
#             visitied[node] = True
#             dfs(node)

# dfs(1)

# if sum(visitied) >= 1:
#     print(sum(visitied)-1)
# else:
#     print(0)