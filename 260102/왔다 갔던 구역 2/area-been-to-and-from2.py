n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.

tmp_list = [0 for _ in range(2001)]
idx_tmp = 1000
for i in range(len(x)):
    idx = x[i]
    direction = dir[i]
    if direction == "R":
        for j in range(idx_tmp, idx_tmp + idx):
            tmp_list[j] += 1
        idx_tmp += idx
    elif direction == "L":
        for j in range(idx_tmp - idx, idx_tmp):
            tmp_list[j] += 1
        idx_tmp -= idx

count = 0
for i in tmp_list:
    if i >= 2:
        count += 1

print(count)