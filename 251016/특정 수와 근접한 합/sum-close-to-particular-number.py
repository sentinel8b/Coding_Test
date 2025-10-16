import sys
INT_MAX_VAL = sys.maxsize

N, S = map(int, input().split())
arr = list(map(int, input().split()))

sum_value = sum(arr)
min_diff = INT_MAX_VAL
# Please write your code here.
for i in range(N):
    for j in range(i+1, N):
        new_sum_val = sum_value - arr[i] - arr[j]
        diff = abs(S - new_sum_val)
        min_diff = min(diff, min_diff)

print(min_diff)