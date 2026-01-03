n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
grid_pad = [[0 for _ in range(n+2)] for _ in range(n+2)]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid_pad[i+1][j+1] = grid[i][j]

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

count = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid_pad[i+1+dx[0]][j+1+dy[0]] + grid_pad[i+1+dx[1]][j+1+dy[1]] + grid_pad[i+1+dx[2]][j+1+dy[2]] + grid_pad[i+1+dx[3]][j+1+dy[3]] >= 3:
            count += 1

print(count)