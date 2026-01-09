n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_count = 0
for i in range(n):
    for j in range(n):
        if j + 2 < n:
            count = grid[i][j] + grid[i][j+1] + grid[i][j+2]
            if count > max_count:
                max_count = count
print(max_count)