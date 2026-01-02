n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
tmp_list = [[0 for _ in range(201)] for _ in range(201)]

for i in range(len(x1)):
    x1_tmp = x1[i] + 100
    y1_tmp = y1[i] + 100
    x2_tmp = x2[i] + 100
    y2_tmp = y2[i] + 100
    for j in range(x1_tmp, x2_tmp):
        for k in range(y1_tmp, y2_tmp):
            tmp_list[j][k] = 1
    
total_size = 0
for i in range(len(tmp_list)):
    for j in range(len(tmp_list[i])):
        if tmp_list[i][j] == 1:
            total_size += 1

print(total_size)