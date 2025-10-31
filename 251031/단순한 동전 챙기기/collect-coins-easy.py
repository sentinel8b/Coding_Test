import sys

n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.
coin_coord = []
start_coord = None
end_coord = None

def calc_dist(coord1, coord2):
    x1, y1 = coord1[0], coord1[1]
    x2, y2 = coord2[0], coord2[1]
    return abs(x2-x1)+abs(y2-y1)

def calc_step():
    num_step = 0
    num_step += calc_dist(start_coord, selected_coin[0][:-1])
    for i in range(len(selected_coin) - 1):
        num_step += calc_dist(selected_coin[i][:-1], selected_coin[i+1][:-1])
    num_step += calc_dist(selected_coin[-1][:-1], end_coord)
    
    return num_step
        
for x in range(n):
    for y in range(n):
        if grid[x][y] == 'S':
            start_coord = (x,y)
        if grid[x][y] == 'E':
            end_coord = (x,y)
        if grid[x][y].isdigit():
            coin_coord.append((x,y,int(grid[x][y])))
            
coin_coord.sort(key=lambda x: x[2])
min_step = sys.maxsize
selected_coin = []

def select(idx, cnt):
    global min_step
    global selected_coin

    if idx == len(coin_coord):
        # 모은 동전이 3개 이상일 때만 거리 계산
        if cnt >= 3:
            case_val = calc_step()
            min_step = min(min_step, case_val)
        return # 여기서만 return해야 함

    if cnt == 0 or coin_coord[idx][2] > selected_coin[-1][2]:
        selected_coin.append(coin_coord[idx])
        select(idx+1, cnt+1)
        selected_coin.pop()

    #pass
    select(idx+1, cnt)

select(0, 0)

if min_step == sys.maxsize:
    print(-1)
else:
    print(min_step)
    
    

