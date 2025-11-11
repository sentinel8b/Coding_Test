def solve():
    n = int(input())
    jobs = []
    
    for _ in range(n):
        s, e, p = map(int, input().split())
        jobs.append((s, e, p))
    
    jobs.sort(key=lambda x: x[1])
    
    dp = [0] * n
    dp[0] = jobs[0][2]
    
    for i in range(1, n):
        not_take = dp[i-1]
        
        take = jobs[i][2]
        for j in range(i-1, -1, -1):
            if jobs[j][1] < jobs[i][0]: 
                take += dp[j]
                break
        
        dp[i] = max(take, not_take)
    
    print(dp[n-1])

solve()
