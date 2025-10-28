n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


def in_range(x, y):
    return 0<=x<n and 0<=y<n

def damage_calc():
    global bomb_order
    global bomb_coord
    cnt = 0
    visited =[[0] * n for _ in range(n)]
    for coord, b_type in zip(bomb_coord, bomb_order):
        x, y = coord
        if not visited[x][y]:
            visited[x][y] = 1
            cnt += 1
        if b_type == 1:
            dxs = dxs_b1
            dys = dys_b1
        if b_type == 2:
            dxs = dxs_b2
            dys = dys_b2
        if b_type == 3:
            dxs = dxs_b3
            dys = dys_b3
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = 1
                cnt += 1
    return cnt
    
# Select bomb shape among 3 block for k(=num of 1) time
dxs_b1 = [-2, -1, 1, 2]
dys_b1 = [0, 0, 0, 0]

dxs_b2 = [-1, 0, 1, 0]
dys_b2 = [0, 1, 0, -1]

dxs_b3 = [-1, -1, 1, 1]
dys_b3 = [-1, 1, 1, -1]

bomb_coord = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bomb_coord.append((i,j))

num_bomb = len(bomb_coord)

max_val = 0
bomb_order = []

def plant_bomb(cur_num):
    global max_val
    if cur_num == num_bomb:
        case_val = damage_calc()
        max_val = max(case_val, max_val)
        return

    for i in range(1,3+1):
        bomb_order.append(i)
        plant_bomb(cur_num+1)
        bomb_order.pop()

plant_bomb(0)

print(max_val)
        
    
