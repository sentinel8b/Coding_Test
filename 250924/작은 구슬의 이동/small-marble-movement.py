n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

def in_range(new_x, new_y):
    return new_x >= 0 and new_x < n and new_y >= 0 and new_y < n

# Please write your code here.
dxs = [0, 1, 0, -1] # R D L U
dys = [1, 0, -1, 0]

mapper = {
    'R' : 0,
    'D' : 1,
    'L' : 2,
    'U' : 3
}

cur_x = r-1
cur_y = c-1
cur_dir = mapper[d]

for _ in range(t):
    dx, dy = dxs[cur_dir], dys[cur_dir]
    new_x = cur_x + dx
    new_y = cur_y + dy
    if not in_range(new_x, new_y):
        #change dir
        cur_dir = cur_dir-2
        if cur_dir < 0:
            cur_dir += 4
    else:
        cur_x = new_x
        cur_y = new_y

print(cur_x+1, cur_y+1)

