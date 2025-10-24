import sys

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

if n==1 and m==1:
    if grid[0][0] >= 0:
        print(1)
        exit()
    else:
        print(-1)
        exit()
        
max_val = -sys.maxsize

def verify_and_calc(x1,x2,y1,y2):
    val = 0
    is_valid = True
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            val+=1
            if grid[x][y] <= 0:
                is_valid = False
    
    return is_valid, val

for x1 in range(n):
    for x2 in range(n):
        for y1 in range(m):
            for y2 in range(m):
                is_valid, val = verify_and_calc(x1,x2,y1,y2)
                if is_valid:
                    max_val = max(max_val, val)

print(max_val)