n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
dir_dict = {"D":0, "L":1, "U":2, "R":3}
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
r -= 1
c -= 1

init_dir = dir_dict[d]
for i in range(t):
    if init_dir == 0 or init_dir == 2:
        if r + dx[init_dir] >= n or r+dx[init_dir] < 0:
            init_dir = (init_dir + 2) % 4
        else:
            r += dx[init_dir]
            c += dy[init_dir]
    elif init_dir == 1 or init_dir == 3:
        if c + dy[init_dir] >= n or c + dy[init_dir] < 0:
            init_dir = (init_dir + 2) % 4
        else:
            r += dx[init_dir]
            c += dy[init_dir]
print(r+1,c+1)
