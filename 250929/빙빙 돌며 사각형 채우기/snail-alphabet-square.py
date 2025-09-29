n, m = map(int, input().split())

# Please write your code here.
grid = [[0] * m for _ in range(n)]

alphabet_string = 'ABCDEFGHIJKLMNOPQRSTVWXYZ'
dxs = [0, 1, 0, -1] # R D L U
dys = [1, 0, -1 ,0]

dir_idx = 0

def in_range(new_x, new_y):
    return new_x >= 0 and new_x < n and new_y >= 0 and new_y < m

x_cur, y_cur = 0, 0

for i in range(0, n*m):
    grid[x_cur][y_cur] = alphabet_string[i%len(alphabet_string)]
    new_x, new_y = x_cur + dxs[dir_idx], y_cur + dys[dir_idx]
    if in_range(new_x, new_y) and grid[new_x][new_y] == 0:
        x_cur, y_cur = new_x, new_y
    else: # turn direction to clock-wise
        dir_idx = (dir_idx + 1)%4
        x_cur = x_cur + dxs[dir_idx]
        y_cur = y_cur + dys[dir_idx]

for i in range(n):
    for j in range(m):
        print(grid[i][j], end = " ")
    print()
