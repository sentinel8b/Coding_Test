N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
result = 0
def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < M

dx, dy = [1, 1, 0, -1, -1, -1, 0, 1], [0, 1, 1, 1, 0 , -1, -1, -1]


for i in range(N):
    for j in range(M):
        if arr[i][j] == "L":
            for k in range(8):
                if in_range(i+dy[k], j+dx[k]) and in_range(i+2*dy[k], j+2*dx[k]):
                    if arr[i+dy[k]][j+dx[k]] == "E" and arr[i+2*dy[k]][j+2*dx[k]] == "E":
                        result += 1
print(result)
            
