x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
OFFSET = 1000
GridSize = 2000

grid = [
    [0] * (GridSize+1) for _ in range(GridSize+1)
    ]

# Place A into grid
x1_coord, x2_coord, y1_coord, y2_coord = x1[0] + OFFSET, x2[0] + OFFSET, y1[0] + OFFSET, y2[0] + OFFSET
for x in range(x1_coord, x2_coord):
    for y in range(y1_coord, y2_coord):
        grid[x][y] = 1

# Place B into grid
x1_coord, x2_coord, y1_coord, y2_coord = x1[1] + OFFSET, x2[1] + OFFSET, y1[1] + OFFSET, y2[1] + OFFSET
for x in range(x1_coord, x2_coord):
    for y in range(y1_coord, y2_coord):
        grid[x][y] = 1        

# Place M into grid
x1_coord, x2_coord, y1_coord, y2_coord = x1[2] + OFFSET, x2[2] + OFFSET, y1[2] + OFFSET, y2[2] + OFFSET
for x in range(x1_coord, x2_coord):
    for y in range(y1_coord, y2_coord):
        grid[x][y] = 0   

ans = 0
for x in range(GridSize+1):
    for y in range(GridSize+1):
        if grid[x][y]:
            ans += 1

print(ans)