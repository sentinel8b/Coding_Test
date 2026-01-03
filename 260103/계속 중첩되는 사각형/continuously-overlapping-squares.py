N = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

tmp_list = [[-1 for _ in range(2001)] for _ in range(2001)]

for n in range(N):
    x1_tmp, x2_tmp, y1_tmp, y2_tmp = x1[n] + 1000, x2[n] + 1000, y1[n] + 1000, y2[n] + 1000

    if n % 2 == 0:
        for i in range(x1_tmp, x2_tmp):
            for j in range(y1_tmp, y2_tmp):
                tmp_list[i][j] = 0
    elif n % 2 == 1:
        for i in range(x1_tmp, x2_tmp):
            for j in range(y1_tmp, y2_tmp):
                tmp_list[i][j] = 1

total_sum = 0
for i in range(len(tmp_list)):
    for j in range(len(tmp_list[i])):
        if tmp_list[i][j] == 1:
            total_sum += tmp_list[i][j]

print(total_sum)