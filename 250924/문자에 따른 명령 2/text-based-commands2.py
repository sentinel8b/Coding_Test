dirs = input()

# Please write your code here.
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

cur_dir = 3
coord_x, coord_y = 0, 0
for char in dirs:
    if char == 'L':
        cur_dir = (cur_dir - 1 + 4)%4
    elif char == 'R':
        cur_dir = (cur_dir + 1)%4
    else: # 'F'
        coord_x += dx[cur_dir]
        coord_y += dy[cur_dir]

print(coord_x, coord_y)