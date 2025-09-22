n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
# grid = [0]*(2000+1)
# start_idx = 100

# for i in range(n):
#     dx = x[i]
#     dir_str = dir[i]
#     if dir_str == 'L':
#         for j in range(start_idx-dx, start_idx):
#             grid[j] += 1
#         start_idx -= dx
#     else:
#         for j in range(start_idx, start_idx+dx):
#             grid[j] += 1
#         start_idx += dx
# val = 0

# for item in grid:
#     if item > 1:
#         val+=1

# print(val)

OFFSET = 1000
MAX_R = 2000

cur = 0
segments = []
for i in range(n):
    dir_str = dir[i]
    dx = x[i]
    if dir_str == "L":
        start_idx = cur - dx
        end_idx = cur
        cur -= dx
    else:
        start_idx = cur
        end_idx = cur + dx
        cur += dx
    segments.append([start_idx, end_idx])

grid = [0] * (MAX_R+1)

for start_idx, end_idx in segments:
    start_idx, end_idx = start_idx+OFFSET, end_idx+OFFSET
    for i in range(start_idx, end_idx):
        grid[i] += 1

val = 0
for item in grid:
    if item >= 2:
        val += 1
print(val)

