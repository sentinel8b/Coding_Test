x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
tmp_list = [[0 for _ in range(2001)] for _ in range(2001)]

for i in range(3):
    x1_tmp = x1[i] + 1000
    y1_tmp = y1[i] + 1000
    x2_tmp = x2[i] + 1000
    y2_tmp = y2[i] + 1000
    if i < 2:
        for j in range(x1_tmp, x2_tmp):
            for k in range(y1_tmp, y2_tmp):
                tmp_list[j][k] = 1
    else:
        for j in range(x1_tmp, x2_tmp):
            for k in range(y1_tmp, y2_tmp):
                tmp_list[j][k] = 0

total_size = 0
for i in range(len(tmp_list)):
    for j in range(len(tmp_list[i])):
        if tmp_list[i][j] == 1:
            total_size += 1
print(total_size)