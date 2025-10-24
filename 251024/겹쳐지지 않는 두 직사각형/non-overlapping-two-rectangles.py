import sys

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def is_cross(x2,x3,y2,y3):
    return x3 <= x2 and y3 <= y2

def calc_val(x1,x2,y1,y2):
    val = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            val += grid[x][y]
    return val if val != 0 else -sys.maxsize

max_val = -sys.maxsize

for x1 in range(n):
    for x2 in range(n):
        for y1 in range(m):
            for y2 in range(m):
                for x3 in range(n):
                    for x4 in range(n):
                        for y3 in range(m):
                            for y4 in range(m):
                                if not is_cross(x2, x3, y2, y3):
                                    grid_sum1 = calc_val(x1,x2,y1,y2)
                                    grid_sum2 = calc_val(x3,x4,y3,y4)
                                    max_val = max(max_val, grid_sum1+grid_sum2)
                                    # if x1 == 0 and y1 == 0 and x2 ==0 and y2 == 0 and x3 == 0 and y3 ==1 and x4 ==0 and y4 == 1:
                                    #     print(grid_sum1, grid_sum2)

print(max_val)


