dirs = input()

# Please write your code here.
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

init_dir = 3
result_x, result_y = 0, 0
for d in dirs:
    if d == "R":
        init_dir = (init_dir + 1) % 4
    elif d == "L":
        init_dir = (init_dir - 1) % 4
    elif d == "F":
        result_x += dx[init_dir]
        result_y += dy[init_dir]

print(result_x,result_y)
