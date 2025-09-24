n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

def in_range(new_x, new_y):
    return new_x >= 0 and new_x < n and new_y >= 0 and new_y < m

# Please write your code here.
dxs = [0, 1, 0, -1] # R D L U
dys = [1, 0, -1, 0]

arr[0][0] = 1
cur_dir = 0
cur_x = 0 
cur_y = 0

for i in range(2, m*n + 1):
    dx = dxs[cur_dir]
    dy = dys[cur_dir]
    new_x = cur_x + dx
    new_y = cur_y + dy
    if not in_range(new_x, new_y) or arr[new_x][new_y] != 0:
        #change dir
        cur_dir = (cur_dir + 1)%4

    dx = dxs[cur_dir]
    dy = dys[cur_dir]
    new_x = cur_x + dx
    new_y = cur_y + dy
    arr[new_x][new_y] = i
    cur_x = new_x
    cur_y = new_y

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()