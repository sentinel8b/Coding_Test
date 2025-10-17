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
for i in range(len(arr)):
    start_idx = i-K
    end_idx = i+K+1

    if start_idx < 0:
        start_idx = 0
    if end_idx > len(arr):
        end_idx = len(arr)

    local_sum = sum(arr[start_idx:end_idx])
    max_val = max(max_val, local_sum)

print(max_val)