n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
grid = [[0] * n for _ in range(n)]

dxs = [0, 1, 0, -1] # R D L U
dys = [1, 0, -1, 0] # R D L U

ans = 0 

def in_range(new_x, new_y):
    return new_x >= 0 and new_y >= 0 and new_x < n and new_y < n

for point in points:
    x, y = point
    # adjust index
    x -= 1
    y -= 1
    grid[x][y] = 1
    cnt = 0
    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy
        if in_range(new_x, new_y) and grid[new_x][new_y] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)
