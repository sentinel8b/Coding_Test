n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import sys

max_val = -sys.maxsize + 1

for i in range(n-k+1):
    sum = 0
    for j in range(k):
        sum += arr[i + j]
    max_val = max(sum, max_val)
print(max_val)