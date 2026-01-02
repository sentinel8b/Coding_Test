n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
color_list = [-1 for _ in range(200001)]
num_list_b = [0 for _ in range(200001)]
num_list_w = [0 for _ in range(200001)]
##0 : Black , 1 : White##
idx_tmp = 100000
for i in range(len(x)):
    idx = x[i]
    direction = dir[i]
    if direction == "R":
        for j in range(idx_tmp, idx_tmp + idx):
            color_list[j] = 0
            num_list_b[j] += 1
        idx_tmp = idx_tmp + idx - 1
    elif direction == "L":
        for j in range(idx_tmp - idx + 1, idx_tmp + 1):
            color_list[j] = 1
            num_list_w[j] += 1
        idx_tmp = idx_tmp -  idx + 1
b_count = 0
w_count = 0
g_count = 0
for i in range(len(color_list)):
    if num_list_b[i] >= 2 and num_list_w[i] >= 2:
        g_count += 1
    else:
        if color_list[i] == 0:
            b_count += 1
        elif color_list[i] == 1:
            w_count += 1

print(w_count, b_count, g_count)