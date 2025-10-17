N, K = map(int, input().split())
candy = []
pos = []

arr = [0] * (100 + 1)

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)
    arr[p] += c

max_val = 0

# Please write your code here.
for i in range(K, len(arr)-K+1):
    local_sum = sum(arr[i-K:i+K+1])
    max_val = max(max_val, local_sum)

print(max_val)