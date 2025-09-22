n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
grid = [0]*(200+1)
start_idx = 100

for i in range(n):
    dx = x[i]
    dir_str = dir[i]
    if dir_str == 'L':
        for j in range(start_idx-dx, start_idx):
            grid[j] += 1
        start_idx -= dx
    else:
        for j in range(start_idx, start_idx+dx):
            grid[j] += 1
        start_idx += dx
val = 0

for item in grid:
    if item > 1:
        val+=1

print(val)