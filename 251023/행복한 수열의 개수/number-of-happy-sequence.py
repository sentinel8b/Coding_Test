n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# edge case
if m == 1:
    print(2*n)
    exit()

cnt = 0
# row based
for i in range(n):
    for j in range(n-m):
        for k in range(m):
            if grid[i][j+k+1] == grid[i][j+k]:
                cnt += 1
                break

# col based
for i in range(n):
    for j in range(n-m):
        for k in range(m):
            if grid[j+k+1][i] == grid[j+k][i]:
                cnt += 1
                break

print(cnt)
