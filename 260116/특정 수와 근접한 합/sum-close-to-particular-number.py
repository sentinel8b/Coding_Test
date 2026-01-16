N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
result = sys.maxsize
for i in range(N):
    for j in range(i+1, N):
        sum = 0
        for a in arr:
            sum += a
        sum = sum - arr[i] - arr[j]
        result = min(result, abs(sum - S))
print(result)