n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys
max_val = -sys.maxsize + 1
for i in range(n-2):
    for j in range(n-2):
        sum = 0
        for k in range(3):
            for w in range(3):
                sum += grid[i+k][j+w]
        max_val = max(max_val, sum)
print(max_val)