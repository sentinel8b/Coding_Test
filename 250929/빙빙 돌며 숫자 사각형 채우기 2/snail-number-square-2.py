n, m = map(int, input().split())

# Please write your code here.
grid = [[0] * m for _ in range(n)]

dxs = [0, 1, 0, -1] # R D L U
dys = [1, 0, -1, 0]

cur_dir = 1

def is_range(new_x, new_y):
    return new_x >= 0 and new_x < n and new_y >= 0 and new_y < m

x_coord, y_coord = 0, 0

for i in range(1, n*m + 1):
    # mark current coord
    grid[x_coord][y_coord] = i
    new_x, new_y = x_coord + dxs[cur_dir], y_coord + dys[cur_dir]
    if is_range(new_x, new_y) and grid[new_x][new_y] == 0:
        x_coord, y_coord = new_x, new_y
    else: # turn to counter-clock wise
        cur_dir = (cur_dir -1 + 4)%4
        x_coord = x_coord + dxs[cur_dir]
        y_coord = y_coord + dys[cur_dir]

for i in range(n):
    for j in range(m):
        print(grid[i][j], end = " ")
    print()

