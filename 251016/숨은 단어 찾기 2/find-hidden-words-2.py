N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
dxs = [-1, -1, 0, 1, 1, 1, 0, -1] # N NE E SE S SW W NW 
dys = [0, 1, 1, 1, 0 ,-1, -1, -1] # N NE E SE S SW W NW 

def in_range(x, y):
    return x >= 0 and y >= 0 and x < N and y < M

total_cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] != 'L':
            continue
        for dx, dy in zip(dxs, dys):
            cur_x, cur_y  = i, j
            cnt_E = 0
            for _ in range(2): # 0, 1
                if in_range(cur_x + dx, cur_y + dy):
                    if arr[cur_x + dx][cur_y + dy] == 'E':
                        cur_x = cur_x + dx
                        cur_y = cur_y + dy
                        cnt_E += 1                       
                else:
                    break

            if cnt_E == 2:
                total_cnt +=1    

print(total_cnt)


