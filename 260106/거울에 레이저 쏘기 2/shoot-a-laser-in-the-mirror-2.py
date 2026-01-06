n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
idx_dict = {}
for i in range(n*4):
    if i // n == 0:
        idx_dict[i] = [0,i % n]
        init_dir = 1
    elif i // n == 1:
        idx_dict[i] = [i % n, n-1]
        init_dir = 2
    elif i // n == 2:
        idx_dict[i] = [n-1, n - 1 - i%n]
        init_dir = 3
    elif i // n == 3:
        idx_dict[i] = [n - 1 - i%n, 0]
        init_dir = 0

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

result = 0
idx_x, idx_y = idx_dict[k-1][0], idx_dict[k-1][1]
init_dir = ((k-1) // n + 1) % 4

while True:
    init_glass = grid[idx_x][idx_y]
    if init_dir % 2 == 1:
        if init_glass == '\\':
            init_dir = (init_dir - 1) % 4
        else:
            init_dir = (init_dir + 1) % 4
    else:
        if init_glass == '\\':
            init_dir = (init_dir + 1) % 4
        else:
            init_dir = (init_dir - 1) % 4
    idx_x += dx[init_dir]
    idx_y += dy[init_dir]
    result += 1
    if idx_x < 0 or idx_y < 0 or idx_x >= n or idx_y >= n:
        break 
print(result)