n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
tmp_list= [[0 for _ in range(201)] for _ in range(201)]

for i in range(n):
    x_tmp = x[i]
    y_tmp = y[i]

    for j in range(x_tmp, x_tmp+8):
        for k in range(y_tmp, y_tmp+8):
            tmp_list[j][k] = 1

total_size = 0
for i in range(len(tmp_list)):
    for j in range(len(tmp_list[i])):
        if tmp_list[i][j] == 1:
            total_size += 1

print(total_size)