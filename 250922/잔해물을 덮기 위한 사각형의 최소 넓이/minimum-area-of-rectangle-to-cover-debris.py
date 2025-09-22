x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

OFFSET = 1000
GridSize = 2000
# Please write your code here.
grid = [
    [0] * (GridSize + 1) for _ in range(GridSize+1)
]

# Place rec 1
x1_coord, x2_coord, y1_coord, y2_coord = x1[0] + OFFSET, x2[0] + OFFSET, y1[0] + OFFSET, y2[0] + OFFSET
for x in range(x1_coord, x2_coord):
    for y in range(y1_coord, y2_coord):
        grid[x][y] = 1

# Place rec 2
x1_coord, x2_coord, y1_coord, y2_coord = x1[1] + OFFSET, x2[1] + OFFSET, y1[1] + OFFSET, y2[1] + OFFSET
for x in range(x1_coord, x2_coord):
    for y in range(y1_coord, y2_coord):
        grid[x][y] = 0

# find min max x&y
x_coords = []
y_coords = []
for x in range(GridSize+1):
    if sum(grid[x]) <= 0:
        continue
    else: # has
        x_coords.append(x)
        for y in range(GridSize+1): 
            if grid[x][y] == 1:
                y_coords.append(y)

dx = max(x_coords) - max(x_coords) + 1
dy = max(y_coords) - min(y_coords) + 1

print(dx*dy)