n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# edge case
if m == 1:
    print(2*n)
    exit()

cnt = 0
# row based
for i in range(n): # 0
    for j in range(n-m): # 0, 1
        local_cnt = 1
        is_found = False
        for k in range(m): # 0, 1, 2
            if grid[i][j+k+1] == grid[i][j+k]:
                local_cnt += 1
                if local_cnt >= m:
                    cnt += 1
                    is_found = True
                    break
            else:
                local_cnt = 1
        if is_found:
            break

# col based
for i in range(n):
    for j in range(n-m):
        local_cnt = 1
        is_found = False
        for k in range(m):
            if grid[j+k+1][i] == grid[j+k][i]:
                local_cnt += 1
                if local_cnt >= m:
                    cnt += 1
                    is_found = True
                    break
            else:
                local_cnt = 1
        if is_found:
            break
            
print(cnt)
