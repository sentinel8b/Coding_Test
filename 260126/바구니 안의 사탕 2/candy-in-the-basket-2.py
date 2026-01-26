N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
import sys

candy_pos = [0 for _ in range(101)]
candy_pos_d  = [0 for _ in range(101)]

for n in range(N):
    candy_pos[pos[n]] = candy[n]
    candy_pos_d[pos[n]] += 1

max_val = -sys.maxsize + 1

for i in range(101):
    if i >= K:
        tmp_candy = candy_pos[i - K : i + K + 1]
        d = candy_pos_d[i - K : i + K + 1]
    if i < K:
        tmp_candy = candy_pos[0 : i + K + 1]
        d = candy_pos_d[0 : i + K + 1]
    sum = 0
    for j in range(len(tmp_candy)):
        sum += tmp_candy[j] * d[j]
    max_val = max(max_val, sum)

print(max_val)