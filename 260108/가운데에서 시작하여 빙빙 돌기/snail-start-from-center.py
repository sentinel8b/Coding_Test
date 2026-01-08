n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
idx_x, idx_y = n - 1 , n - 1
init_dir = 0
tmp_val = n * n
for i in range(n):
    for j in range(n):
        grid[idx_x][idx_y] = tmp_val
        next_x = idx_x + dx[init_dir]
        next_y = idx_y + dy[init_dir]
        if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n and grid[next_x][next_y] == 0:
            idx_x = next_x
            idx_y = next_y
        else:
            init_dir = (init_dir + 1) % 4
            idx_x += dx[init_dir]
            idx_y += dy[init_dir]
        tmp_val -= 1

for i in range(n):
    for j in range(n):
        if j == n-1:
            print(grid[i][j])
        else:
            print(grid[i][j], end=" ")
