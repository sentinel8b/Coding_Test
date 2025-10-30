n = int(input())
val_grid = [list(map(int, input().split())) for _ in range(n)]
dir_grid = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int,input().split())
#adjust to 0-based idx
x, y = x-1, y-1

dxs = [0] + [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0] + [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

max_cnt = 0

def move(x, y, cnt):
    global max_cnt
    dir_idx = dir_grid[x][y]
    dx = dxs[dir_idx]
    dy = dys[dir_idx]

    # if cnt == n:
    #     max_cnt = max(max_cnt, cnt)
    #     return

    for i in range(1,n):
        dx = i*dxs[dir_idx]
        dy = i*dys[dir_idx]
        if not in_range(x+dx, y+dy):
            continue
        if val_grid[x+dx][y+dy] < val_grid[x][y]:
            continue
        move(x+dx, y+dy, cnt+1)

    max_cnt = max(max_cnt, cnt)

move(x, y, 0)

print(max_cnt)
