n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

color_list = [-1 for _ in range(200001)]

idx = 100000
# Black : 0 , White : 1
for i in range(len(x)):
    idx_tmp = x[i]
    direction = dir[i]

    if direction == "R":
        for j in range(idx, idx+idx_tmp):
            color_list[j] = 0
        idx = idx + idx_tmp - 1
    elif direction == "L":
        for j in range(idx-idx_tmp+1, idx+1):
            color_list[j] = 1
        idx = idx - idx_tmp + 1

b_count = 0
w_count = 0
for i in color_list:
    if i == 0:
        b_count += 1
    elif i == 1:
        w_count += 1
print(w_count, b_count)