n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def get_gold(x, y, k):
    cnt_gold = 0
    for i in range(n):
        for j in range(n):
            if abs(x-i)+abs(y-j) <= k:
                if grid[i][j] == 1:
                    cnt_gold +=1
    return cnt_gold


max_gold_found = 0
k = 0

while True:
    if (n**2)*m < k**2 + (k+1)**2:
        break

    for x in range(n):
        for y in range(n):
            earned_gold = get_gold(x, y, k)
            cost = k**2 + (k+1)**2
            margin = earned_gold*m - cost
            if margin >= 0:
                max_gold_found = max(max_gold_found, earned_gold)
    k+=1
print(max_gold_found)
