n = int(input())
num_seq = list(map(int, input().split()))
num_seq = [0] + num_seq

dp = [0] * (n+1)

for i in range(1,n+1):
    for j in range(i):
        if num_seq[i] > num_seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))