n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [0, 1, 0, -1] # R D L U
dys = [1, 0, -1, 0]

def in_range(new_x, new_y):
    return 0 <= new_x and new_x < n and 0 <= new_y and new_y < n
cnt = 0
for x in range(n):
    for y in range(n):
        in_loop_cnt = 0
        for dx, dy in zip(dxs, dys):
            new_x = x + dx
            new_y = y + dy
            if in_range(new_x, new_y) and grid[new_x][new_y] == 1:
                in_loop_cnt += 1
        if in_loop_cnt >= 3:
            cnt +=1
print(cnt)