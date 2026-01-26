N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.

import sys
max_val = -sys.maxsize + 1

sorted_pos = sorted(pos)
min_idx, max_idx = sorted_pos[0], sorted_pos[-1]

for i in range(min_idx+K, max_idx-K+1):
    sum = 0
    for j in range(len(pos)):
        p = pos[j]
        if p >= i-K and p <= i + K:
            sum += candy[j]
    max_val = max(max_val, sum)
print(max_val)