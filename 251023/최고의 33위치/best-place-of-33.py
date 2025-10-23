n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return x>=0 and x < n and y>=0 and y<n

# U UR R DR D DL L UL 
dxs = [-1, -1, 0, 1, 1, 1, 0, -1] 
dys = [0, 1, 1, 1, 0, -1, -1 ,-1]

max_val = 0

for x in range(1, n-1):
    for y in range(1, n-1):
        grid_sum = grid[x][y]
        valid_flag = True
        for dx, dy in zip(dxs, dys):
            new_x = x + dx
            new_y = y + dy
            if in_range(new_x, new_y):
                grid_sum += grid[new_x][new_y]
            else:
                valid_flag = False
                break
        if valid_flag:
            max_val = max(max_val, grid_sum)

print(max_val)