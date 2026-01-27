n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys

max_b1 = -sys.maxsize + 1
for i in range(n):
    for j in range(n):
        if j + 2 < n:
            sum = grid[i][j] + grid[i][j+1] + grid[i][j+2]
            max_b1 = max(max_b1, sum)
        if i + 2 < n:
            sum = grid[i][j] + grid[i+1][j] + grid[i+2][j]
            max_b1 = max(max_b1, sum)

max_b2 = -sys.maxsize + 1
for i in range(n):
    for j in range(n):
        if i+1 < n and j+1 < n:
            sum1 = grid[i][j] + grid[i+1][j] + grid[i+1][j+1]
            sum2 = grid[i][j] + grid[i][j+1] + grid[i+1][j+1]
            max_val = max(sum1, sum2)
            max_b2 = max(max_b2, max_val)
        if i-1 >= 0 and j+1 < n:
            sum1 = grid[i][j] + grid[i][j+1] + grid[i-1][j+1]
            sum2 = grid[i][j] + grid[i-1][j] + grid[i-1][j+1]
            max_val = max(sum1, sum2)
            max_b2 = max(max_b2, max_val)
        if i-1 >= 0 and j-1 >= 0:
            sum1 = grid[i][j] + grid[i][j-1] + grid[i-1][j-1]
            sum2 = grid[i][j] + grid[i-1][j] + grid[i-1][j-1]
            max_val = max(sum1, sum2)
            max_b2 = max(max_b2, max_val)
        if i+1 < n and j-1 >= 0:
            sum1 = grid[i][j] + grid[i+1][j] + grid[i+1][j-1]
            sum2 = grid[i][j] + grid[i][j-1] + grid[i+1][j-1]
            max_val = max(sum1, sum2)
            max_b2 = max(max_b2, max_val)

print(max(max_b1, max_b2))