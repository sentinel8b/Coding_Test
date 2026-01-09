n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
import sys
max_cost = -sys.maxsize

for i in range(n):
    cost = 0
    for j in range(n):
        if i >= j:
            cost += (i - j) * A[j]
        else:
            cost += (j - i) * A[j]
    if cost < max_cost:
        max_cost = cost
print(max_cost)