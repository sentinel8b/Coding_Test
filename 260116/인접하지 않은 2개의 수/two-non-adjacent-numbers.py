n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
import sys
max_val = -sys.maxsize + 1
for i in range(n-2):
    for j in range(i+2, n):
        max_val = max(max_val, numbers[i] + numbers[j])
print(max_val)
