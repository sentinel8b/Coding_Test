N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
min_val = sys.maxsize

for i in range(N - T + 1):
    tmp_arr = arr[i:i+T]
    total_cnt = 0
    for t in tmp_arr:
        total_cnt += abs(t-H)
    min_val = min(min_val, total_cnt)
print(min_val)