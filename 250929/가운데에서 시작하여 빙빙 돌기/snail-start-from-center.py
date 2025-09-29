n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
dxs = [0, 1, 0, -1] # R D L U
dys = [1, 0, -1, 0]

def in_range(new_x, new_y):
    return new_x >= 0 and new_x < n and new_y >= 0 and new_y < n

# dir_idx = 2

# cur_x, cur_y = n-1, n-1

# for i in range(n*n, 0, -1):
#     grid[cur_x][cur_y] = i
#     new_x = cur_x + dxs[dir_idx]
#     new_y = cur_y + dys[dir_idx]
#     if in_range(new_x, new_y) and grid[new_x][new_y] == 0:
#         cur_x, cur_y = new_x, new_y
#     else:
#         dir_idx = (dir_idx + 1)%4
#         cur_x = cur_x + dxs[dir_idx]
#         cur_y = cur_y + dys[dir_idx]

# for i in range(n):
#     for j in range(n):
#         print(grid[i][j], end = " ")
#     print()

cur_x, cur_y = n//2, n//2
dir_idx = 0
move_step = 1

cnt = 1

while True:
    if not in_range(cur_x, cur_y):
        break

    for _ in range(move_step):
        grid[cur_x][cur_y] = cnt
        cnt += 1

        new_x = cur_x + dxs[dir_idx]
        new_y = cur_y + dys[dir_idx]
        if in_range(new_x, new_y):
            cur_x, cur_y = new_x, new_y
        else: #change dir R -> U -> L -> D
            cur_x, cur_y = new_x, new_y
            break
    
    dir_idx = (dir_idx - 1 + 4)%4

    if dir_idx == 0 or dir_idx == 2:
        move_step += 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end = " ")
    print()