n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
dxs = [0, 1, 0, -1] # R D L U
dys = [1, 0, -1, 0]

dir_idx = None
# get dir and initialize x,y from k
if k <= n:
    dir_idx = 1
    x, y = 0, k-1
elif k <= 2*n:
    dir_idx = 2
    x, y = (k%n)-1 , n-1
    if k == 2*n:
        x = n-1
elif k <= 3*n:
    dir_idx = 3
    x = n-1
    y = n-(k%n)
else:
    dir_idx = 0
    x = n-(k%n)
    y = 0

def in_range(new_x, new_y):
    return new_x >= 0 and new_x < n and new_y >= 0 and new_y < n

ans = 0

while True:
    ans += 1
    if grid[x][y] == '/': 
        if dir_idx == 0 or dir_idx == 2: # L or R => 90' turn to counter clock-wise
            dir_idx = (dir_idx - 1 + 4)%4
        else: # U or D => 90' turn to clock-wise
            dir_idx = (dir_idx+1)%4
    else: # '\'
        if dir_idx == 0 or dir_idx == 2:
            dir_idx = (dir_idx+1)%4
        else:
            dir_idx = (dir_idx - 1 + 4)%4
    if in_range(x + dxs[dir_idx], y + dys[dir_idx]):
        x = x + dxs[dir_idx]
        y = y + dys[dir_idx]
    else:
        print(ans)
        break