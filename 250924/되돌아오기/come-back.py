N = int(input())

dxs = [1, 0, -1, 0] # R D L U
dys = [0, -1, 0, 1] # R D L U

dir_mapper = {
    'E' : 0,
    'S' : 1,
    'W' : 2,
    'N' : 3
}

cur_x, cur_y = 0, 0
accum_time = 0
for i in range(N):
    dir_str, diff = input().split()
    diff = int(diff)
    dir_idx = dir_mapper[dir_str]
    for j in range(diff):
        dx, dy = dxs[dir_idx], dys[dir_idx]
        cur_x += dx
        cur_y += dy
        accum_time += 1
        if cur_x == 0 and cur_y == 0:
            print(accum_time)
            exit(0)
else:
    print(-1)

