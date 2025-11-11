n = int(input())
num_seq = list(map(int, input().split()))

dp = [0] * n

for i in range(1,n):
    for j in range(i):
        if num_seq[i] > num_seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)

ans = 0
for i in range(len(dp)):
    ans = max(ans, dp[i])

print(ans+1)