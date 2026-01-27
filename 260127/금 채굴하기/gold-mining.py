n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

results = 0

for K in range(50):
    max_fee = 0
    for i in range(n):
        for j in range(n):
            tmp_fee = 0
            total_num = 0
            for k in range(-K,K+1):
                for w in range(-K,K+1):
                    if abs(k) + abs(w) <= K and i+k >= 0 and i+k < n and j+w >= 0 and j+w < n:
                        tmp_fee += grid[i+k][j+w] * m
                        total_num += grid[i+k][j+w]
            max_fee = max(max_fee, tmp_fee - (K**2 + (K+1)**2))
            if tmp_fee >= (K**2 + (K+1)**2):
                results = max(total_num, results)

print(results)
