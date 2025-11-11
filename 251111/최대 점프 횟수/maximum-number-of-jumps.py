import sys

INT_MIN = -sys.maxsize

n = int(input())

num_seq = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    dp[i] = INT_MIN
dp[0] = 0

for i in range(1,n):
    for j in range(i):
        if dp[j] == INT_MIN:
            continue
        
        if j + num_seq[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
