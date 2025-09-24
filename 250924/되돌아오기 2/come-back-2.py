commands = input()

# Please write your code here.
dx = [1, 0, -1, 0] # R D L U
dy = [0, -1, 0, 1]

cur_dir_idx = 3
cur_x, cur_y = 0, 0
accum_time = 0
for char in commands:
    if char == 'L':
        cur_dir_idx = (cur_dir_idx - 1 + 4)%4
    elif char == 'R':
        cur_dir_idx = (cur_dir_idx+1)%4
    else: # F
        cur_x += dx[cur_dir_idx]
        cur_y += dy[cur_dir_idx]

    accum_time+=1
    
    if cur_x == 0 and cur_y == 0:
        print(accum_time)
        exit(0)
else:
    print(-1)