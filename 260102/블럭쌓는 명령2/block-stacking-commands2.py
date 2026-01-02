n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
tmp_list = [0 for _ in range(n+1)]

for (idx1, idx2) in commands:
    for i in range(idx1, idx2+1):
        tmp_list[i] += 1

max_val = 0
for i in tmp_list:
    if max_val < i:
        max_val = i
print(max_val)