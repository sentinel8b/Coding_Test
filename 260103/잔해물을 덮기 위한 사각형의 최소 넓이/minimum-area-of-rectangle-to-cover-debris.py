x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

tmp_list = [[0 for _ in range(2001)] for _ in range(2001)]

for i in range(x1[0] + 1000, x2[0] + 1000):
    for j in range(y1[0] + 1000, y2[0] + 1000):
        tmp_list[i][j] = 1

for i in range(x1[1] + 1000, x2[1] + 1000):
    for j in range(y1[1] + 1000, y2[1] + 1000):
        tmp_list[i][j] = 0

total_sum = 0
lx, rx, by, ty = 2001, 0, 2001, 0

for i in range(len(tmp_list)):
    for j in range(len(tmp_list[i])):
        if tmp_list[i][j] == 1:
            if i < lx:
                lx = i
            if i > rx:
                rx = i
            if j < by:
                by = j
            if j > ty:
                ty = j
if lx == 2001:
    print(0)
else:
    print((rx - lx + 1) * (ty - by + 1))
