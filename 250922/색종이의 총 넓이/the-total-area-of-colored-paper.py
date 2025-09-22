n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]


# Please write your code here.
GridSize = 200
OFFSET = 100
grid = [
    [0] * (GridSize + 1) for _ in range(GridSize+1)
]

for i in range(len(points)):
    x_coord = points[i][0] + OFFSET
    y_coord = points[i][1] + OFFSET
    for x in range(x_coord, x_coord+8):
        for y in range(y_coord, y_coord+8):
            grid[x][y] += 1

val = 0
for x in range(GridSize+1):
    for y in range(GridSize+1):
        if grid[x][y]>=1:
            val += 1

print(val)
